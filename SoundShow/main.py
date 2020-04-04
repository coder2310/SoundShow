import os
import time
import uuid
import sys
from functools import wraps
import pymysql.cursors
import ThreadEngines
from flask import (Flask, redirect, render_template, request, send_file,
                   session, url_for)


from Utilities import querys, tables, utilities, variables
sound_show = Flask(__name__)
sound_show.secret_key = "super secret key"
sound_show_conn = pymysql.connect(**variables.DB_CONN)


def login_required(function):
    @wraps(function)
    def dec(*args, **kwargs):
        if not "username" in session:
            return redirect(url_for("login"))
        return function(*args, **kwargs)
    return dec


def execute_query(query, return_type=None, parameters=None):
    with sound_show_conn.cursor() as cursor:
        cursor.execute(query, parameters)
    if return_type == "one":
        return cursor.fetchone()
    if return_type == "many":
        return cursor.fetchmany()
    if return_type == "all":
        return cursor.fetchall()
    return None


@login_required
def jsonify_curr_user():
    pass  # this will be used to render a users profile


def retrieve_top_categories(rows=10):
    return execute_query(querys.RETRIEVE_TOP_CONTENT, "all", rows)

# made it function so when we fix up our file structure


def run_sound_show(clear_users=False):
    if clear_users:
        # since its a forign key constrain
        execute_query("DELETE FROM user_interests;")
        execute_query("DELETE FROM user;")
        execute_query(querys.RESET_CONTENT_COUNT)
    sound_show.run(debug=True, threaded =True, host='0.0.0.0')


def recreate_tables():
    try:
        execute_query(tables.USER)
        execute_query(tables.CATEGORY)
        execute_query(tables.CONTENT)
        execute_query(tables.USER_INTERESTS)
        execute_query(tables.NUM_INTERESTED_VIEW)
    except:
        pass


@sound_show.route("/")
def index():
    # if "username" in session:
    #     return redirect(url_for("user_home")) # will implement this
    # once we add log out
    return render_template("index.html")


@sound_show.route("/login")
def login():
    return render_template("login.html")


@login_required
@sound_show.route("/new_user/<curr_uuid>/<name>")
def new_user(curr_uuid, name):
    # First they will select categoirs they are interested
    # will pull list of categories from varaibles
    # that list will then be used to pass in to the new_user.html page
    # will focus on UX later and better routing later just want basic
    # functionality first
    return render_template("new_user.html", curr_uuid=curr_uuid,
                           user_name=session["username"], name=name)


@login_required
@sound_show.route("/insert_categories/<curr_uuid>/<name>")
def insert_categories(curr_uuid, name):
    categor = variables.CATEGORIES
    print(categor, file = sys.stdout)
    return render_template("insert_categories.html", curr_uuid=curr_uuid,
                           user_name=session["username"], name=name, categor=categor)


@login_required
@sound_show.route("/add_content/<curr_uuid>/<name>")
def add_content(curr_uuid, name):
    return render_template("content.html", curr_uuid=curr_uuid, user_name=session["username"],
                           name=name, categories=retrieve_intial_content())


@login_required
def retrieve_intial_content():
    '''Retrieve content from sessiion varaible'''
    # this function can be used for a few things
    # when the user is going thru the registration proccess and its time
    # for them to select more specific content,
    # session["categories"] is the session variable that holds the
    # categories a user is interested in, will use this to retrieve all the content
    # related to that category, we can just use the file in varaibles
    categories = {}
    for cats in session["categories"]:
        categories[cats] = variables.CONTENT[cats]
    return categories


@login_required
@sound_show.route("/insert_new_user_categories", methods=["POST"])
def insert_new_user_categories():
    '''This function will store the categories a user selected 
    as a session varaible, no need to store this information in the data base, since we arent 
    really doing much with this information'''
    if request.form:
        # since the ids in the form are the same
        # as VARIABLES.categories i should be able to loop over those
        session["categories"] = []
        for cats in variables.CATEGORIES:
            # since we already have the name we can check to see if
            # its been selected, using the following line.
            # If its been selected then we can go ahead and add it to the session variable
            print(request.form.getlist(cats), file = sys.stdout)
            selected = bool(request.form.getlist(cats))
            if selected:
                session["categories"].append(cats)
        return redirect(url_for("add_content", curr_uuid=session["uuid"], name=session["username"]))

    # return redirect(url_for("new_user", user_name = session["username"], name = ))


@sound_show.route("/info")
def info():
    return render_template("info.html")


@login_required
def populate_home_page():
    users_interests = execute_query(  # this query returns a list of
        # dictionaries, where the value of each dictionary
        # is one of the users interests
        querys.GET_USERS_INTERESTS, "all", session["username"])
    interests = []  # this where we will populate those values
    if len(users_interests) == 0:  # if the user had not selected any intial interests
        # then we select the default_interests from the database,
        # will probably adjust this so that it will only pick the top content
        # related to their category, but there is also the possibility that
        # they didnt pick any categories, but for now this works
        default_interests = execute_query(
            querys.RETRIEVE_TOP_CONTENT, "all", 10)
        # default also is in the same format as users_interests
        for obj in default_interests:
            # for each of the dictionaries in the
            interests.extend(obj.values())
            # list of query results we call.values() whichh will return a list of
            # values, and we extend that to the interests
        return ThreadEngines.retrieve_content(interests)  
    # we repeat the same steps if the user has selected initial interests
    for obj in users_interests:
        interests.extend(obj.values())
   
    return ThreadEngines.retrieve_content(interests)


@login_required
@sound_show.route("/user_home/<curr_uuid>")
def user_home(curr_uuid):
    '''If the user hasnt selected any content yet, we automatticaly pick the top
    10 and display it with out storing it in the users interests, other wise we display
    everything the user is interested in.
    This is where we would make calls to the APIs with all the data needed.'''
    return render_template("user_home.html", user_name=session["username"], data=populate_home_page())


@sound_show.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@sound_show.route("/login_auth", methods=["POST"])
def login_auth():
    '''Authenticate and validate user'''
    if request.form:
        login_form = request.form
        user_name = request.form["user_name"]
        pass_word = utilities.hash_password(login_form["pass_word"])
        exists = execute_query(
            querys.AUTH_LOGIN, "one", (user_name, pass_word))
        if exists:
            session["username"] = user_name
            session["uuid"] = execute_query(
                querys.GET_UUID, "one", user_name)["uuid"]
            return redirect(url_for("user_home", curr_uuid=session["uuid"]))
        error = "Username or password does not match our records"
        return render_template("login.html", error=error)


@sound_show.route("/reg_auth", methods=["POST"])
def reg_auth():
    '''Register user into system'''
    if request.form:
        register_form = request.form
        user_name = register_form["user_name"]
        pass_word = register_form["pass_word"]
        user_name = user_name.lower()
        if not utilities.valid_username(user_name):
            error = "Username does not satisify requirments"
            return render_template("register.html", error=error)
        if execute_query(querys.USER_EXISTS, "one", (user_name)):
            error = "User already Exists"
            return render_template("register.html", error=error)
        if not utilities.valid_password(pass_word):
            error = "Password does not satify requirments"
            return render_template("register.html", error=error)
        pass_word = utilities.hash_password(register_form["pass_word"])
        first_name = register_form["first_name"]
        last_name = register_form["last_name"]
        user_uuid = str(uuid.uuid4())
        joined = time.strftime('%Y-%m-%d %H:%M:%S')
        fields = (first_name, last_name, user_name,
                  pass_word,  user_uuid, joined)
        # will make a password strength checker later
        execute_query(querys.INSERT_USER, None, fields)
        session["username"] = user_name
        session["uuid"] = user_uuid
        return redirect(url_for("new_user", curr_uuid=session["uuid"], name=first_name))


@login_required
@sound_show.route("/add_user_content", methods=["POST"])
def add_user_content():
    """Add the content the user selected to the table"""
    if request.form:
        for cats in session["categories"]:
            for conts in variables.CONTENT[cats]:
                selected = bool(request.form.getlist(conts))
                if selected:
                    execute_query(querys.ADD_INTEREST, None,
                                  (session["username"], session["uuid"], conts))
                    execute_query(querys.INCREASE_CONTENT_COUNT, None, conts)
                    # now we have to add this to the database
        return redirect(url_for("user_home", curr_uuid=session["uuid"]))


@login_required
@sound_show.route("/profile/<curr_uuid>")
def profile(curr_uuid):
    '''Render the profile of the user with all the data needed'''
    return render_template("profile.html", curr_uuid=curr_uuid, user_name=session["username"],
                           data=jsonify_curr_user())


def insert_content():
    """Use if you want to reinsert content into content table"""
    try:
        execute_query("DELETE FROM content")
        for catergor in sorted(variables.CONTENT.keys()):
            for conts in variables.CONTENT[catergor]:
                execute_query(querys.ADD_CONTENT, None, (conts, catergor))
    except:
        pass


if __name__ == "__main__":
    # will try to come with a query that removes the table if it already
    # exists. Insertign all information from it, into the new table
    # this is just so that if we make changes to the colomuns or constraints
    # run_sound_show()
    try:
        execute_query(querys.RESET_CONTENT_COUNT)
        execute_query(tables.USER_INTERESTS)
    except:
        pass
    run_sound_show(True)

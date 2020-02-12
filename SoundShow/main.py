import os
import time
import uuid
from functools import wraps

import pymysql.cursors
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

@sound_show.route("/")
def index():
    # if "username" in session:
    #     return redirect(url_for("user_home")) # will implement this
    # once we add log out
    return render_template("index.html")


@sound_show.route("/login")
def login():
    return render_template("login.html",)


@login_required
@sound_show.route("/new_user/<curr_uuid>/<name>")
def new_user(curr_uuid, name):
    return render_template("new_user.html", user_name=session["username"], name=name)


@sound_show.route("/info")
def info():
    return render_template("info.html")


@login_required
@sound_show.route("/user_home/<curr_uuid>")
def user_home(curr_uuid):
    return render_template("user_home.html", user_name=session["username"])


@sound_show.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@sound_show.route("/login_auth", methods=["POST"])
def login_auth():
    if request.form:
        login_form = request.form
        user_name = request.form["user_name"]
        pass_word = utilities.hash_password(login_form["pass_word"])
        exists = execute_query(
            querys.AUTH_LOGIN, "one", (user_name, pass_word))
        if exists:
            session["username"] = user_name
            results = execute_query(querys.GET_UUID, "one", user_name)
            return redirect(url_for("user_home", curr_uuid=results["uuid"]))
        error = "Username or password does not match our records"
        return render_template("login.html", error=error)


@sound_show.route("/reg_auth", methods=["POST"])
def reg_auth():
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
        return redirect(url_for("new_user", curr_uuid=user_uuid, name=first_name))

def run_sound_show(): # made it function so when we fix up our file structure
    #its easier to uses
    #execute_query(querys.DROP_TABLE.format("user_interests"))
    #execute_query(querys.DROP_TABLE.format("category"))
    execute_query(tables.user)
    execute_query(tables.category)
    execute_query(tables.content)
    execute_query(tables.user_interests)
    sound_show.run(debug=True)


if __name__ == "__main__":
    # will try to come with a query that removes the table if it already
    # exists. Insertign all information from it, into thew new table
    # this is just so that if we make changes to the colomuns or constraints
    run_sound_show()

import os
import time
import uuid
from functools import wraps

import pymysql.cursors
from flask import (Flask, redirect, render_template, request, send_file,
                   session, url_for)

import querys
import tables
import useful
import variables

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


def retrieve_results(query, return_type=None, parameters=None):
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
        pass_word = useful.hash_password(login_form["pass_word"])
        exists = retrieve_results(
            querys.AUTH_LOGIN, "one", (user_name, pass_word))
        if exists:
            session["username"] = user_name
            results = retrieve_results(querys.GET_UUID, "one", user_name)
            return redirect(url_for("user_home", curr_uuid=results["uuid"]))
        error = "Username or password does not match our records"
        return render_template("login.html", error=error)


@sound_show.route("/reg_auth", methods=["POST"])
def reg_auth():
    if request.form:
        register_form = request.form
        user_name = register_form["user_name"]
        if retrieve_results(querys.USER_EXISTS, "one", (user_name)):
            error = "User already Exists"
            return render_template("register.html", error=error)
        pass_word = useful.hash_password(register_form["pass_word"])
        first_name = register_form["first_name"]
        last_name = register_form["last_name"]
        user_uuid = str(uuid.uuid4())
        joined = time.strftime('%Y-%m-%d %H:%M:%S')
        fields = (first_name, last_name, user_name,
                  pass_word,  user_uuid, joined)
        # will make a password strength checker later
        retrieve_results(querys.INSERT_USER, "all", fields)
        return redirect(url_for("login"))


if __name__ == "__main__":
    retrieve_results(tables.user)
    sound_show.run(debug=True)

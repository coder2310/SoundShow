import constants
import hashlib
import os
import time
import uuid
from functools import wraps

import pymysql.cursors
from flask import (Flask, redirect, render_template, request, send_file,
                   session, url_for)

sound_show = Flask(__name__)
sound_show.secret_key = "super secret key"
db_conn = pymysql.connect(**constants.DB_CONN)
@sound_show.route("/")
def start():
    return "This is Sound Show"

if __name__ == "__main__":
    sound_show.run(debug = True)

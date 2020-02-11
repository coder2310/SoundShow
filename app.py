import random
import string

from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import hashlib
from datetime import date


public1 = 0
public2 = 0

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL
conn = pymysql.connect(host='localhost',
                       port=8889,
                       user='root',
                       password='root',
                       db='SoundShow',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


# Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html', posts=public())


# Define route for login
@app.route('/login')
def login():
    return render_template('login.html')


# Define route for register
@app.route('/register')
def register():
    return render_template('register.html')


# Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    # grabs information from the forms
    User_Name = request.form['User_Name']
    password = request.form['Password'].encode('utf-8')
    hashedPass = hashlib.sha256()
    hashedPass.update(password)
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM User_Info WHERE User_Name = %s and Password = %s'
    cursor.execute(query, (User_Name, hashedPass.hexdigest()))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['User_Name'] = User_Name
        return redirect(url_for('home'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login.html', error=error)


# Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    lower_upper_alphabet = string.ascii_letters
    random_letter = random.choice(lower_upper_alphabet)
    today = str(date.today())
    # grabs information from the forms
    User_Name = request.form['User_Name']
    Password = request.form['Password'].encode('utf-8')
    First_Name = request.form['First_Name']
    Last_Name = request.form['Last_Name']
    hashedPass = hashlib.sha256()
    hashedPass.update(Password)
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query1 = 'SELECT count(*) from User_Info'
    p = cursor.execute(query1)
    # stores the results in a variable

    query = 'SELECT * FROM User_Info WHERE User_Name = %s'
    cursor.execute(query, (User_Name))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error=error)
    else:
        ins = "INSERT INTO User_Info VALUES(%s, %s,%s,%s,%s, %s, 'horror', 0)"
        cursor.execute(ins, (str(p+1)+random_letter+random.choice(lower_upper_alphabet)+random.choice(lower_upper_alphabet),
                             User_Name, hashedPass.hexdigest(), First_Name, Last_Name, today))

        conn.commit()
        cursor.close()
        return render_template('index.html')


@app.route('/public')
def public():
    cursor = conn.cursor();
    query = 'SELECT  * from User_Info '
    cursor.execute(query)
    datas = cursor.fetchall()
    cursor.close()
    return datas


@app.route('/home')
def home():
    User_Name = session['User_Name']
    cursor = conn.cursor();
    query = 'SELECT User_Name, contents from User_Info  WHERE User_Name = %s '
    cursor.execute(query, (User_Name))
    data = cursor.fetchall()
    cursor.close()
    return render_template('home.html', User_Name=User_Name, posts=data)


@app.route('/logout')
def logout():
    session.pop('User_Name')
    return redirect('/')



app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)

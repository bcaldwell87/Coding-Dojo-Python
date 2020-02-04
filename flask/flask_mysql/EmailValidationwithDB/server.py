from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnection
import datetime
import re

app = Flask(__name__)
app.secret_key = "BCBCBC"
mysql = MySQLConnection('email_validation')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show')
def success():
    query = "SELECT * FROM users"                           
    users_list = mysql.query_db(query)                           
    return render_template('show.html', users=users_list) 

@app.route('/process', methods=['POST'])
def process():
    error = False

    # EMAIL VALIDATION
    if len(request.form['email']) < 1:
        flash("Email Address cannot be blank")
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        error = True

    if error == True:
        return redirect('/')
    if error == False:
        if request.form['formAction'] == 'Add Email':
            # Add Email
            query = "INSERT INTO users (email, created_at) VALUES (:email, NOW())"  
            data = {
                'email': request.form['email'],
            }
            mysql.query_db(query, data)
            flash("Email Address: " + request.form['email'] + " was added to the system")
            return redirect('/show')
        if request.form['formAction'] == 'Delete Email':
            # Delete Email DELETE FROM table_name WHERE condition;
            query = "DELETE FROM users WHERE email_address = :email_address"
            data = {
                'email': request.form['email'],
            }
            mysql.query_db(query, data)
            flash("Email Address: " + request.form['email'] + " was removed from the system")
            return redirect('/show')
        


app.run(debug=True)
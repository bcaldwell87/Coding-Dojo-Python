from flask_bcrypt import Bcrypt
import re
import datetime
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "BCBCBC"
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    errors = False
    if len(request.form['name']) < 2:
        flash("Name must be at least 2 characters")
        errors = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be valid")
        errors = True
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
    if request.form['password'] != request.form['confirm_password']:
        flash("Passwords must match")
        errors = True

    if errors:
        return redirect("/")

    query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES (%(n)s, %(e)s, %(p)s, NOW(), NOW());"
    data = {
        "n": request.form["name"],
        "e": request.form["email"],
        "p": bcrypt.generate_password_hash(request.form["password"])
    }
    mysql = connectToMySQL("login_and_registration")
    user_id = mysql.query_db(query, data)
    session['user_id'] = user_id
    session['user_name'] = request.form['name']
    return redirect("/success")


@app.route("/login", methods=["POST"])
def login():
    errors = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be valid")
        errors = True
    if len(request.form['password']) < 1:
        flash("Must provide a password")
        errors = True

    if errors:
        return redirect("/")

    query = "SELECT * FROM users WHERE email = %(e)s;"
    data = {
        "e": request.form['email']
    }
    mysql = connectToMySQL("login_and_registration")
    results = mysql.query_db(query, data)
    print(results)
    if len(results) > 0:
        if bcrypt.check_password_hash(results[0]['password'], request.form['password']):
            session['user_id'] = results[0]["user_id"]
            session['user_name'] = results[0]['name']
            return redirect("/wall")
        else:
            flash("Email/Password combination is incorrect")
            return redirect("/")
    else:
        return redirect("/")


@app.route("/wall")
def wall():
    if not 'user_id' in session:
        flash("You're not logged in")
        return redirect("/")

    query = "SELECT * FROM users WHERE user_id != %(user_id)s;"
    data = {
        'user_id': session['user_id']
    }
    mysql = connectToMySQL("login_and_registration")
    users = mysql.query_db(query, data)
    print(users)

    query = """ SELECT messages.context, messages.id, users.name, messages.created_at
                FROM messages 
                    JOIN users ON messages.sender_id = users.user_id 
                WHERE receiver_id = %(r_id)s;"""
    data = {
        'r_id': session["user_id"]
    }
    mysql = connectToMySQL("login_and_registration")
    messages = mysql.query_db(query, data)
    print(messages)

    return render_template("thewall.html", all_users=users, all_messages=messages, total_messages=len(messages))


@app.route("/messages/create", methods=["POST"])
def create_message():
    if not 'user_id' in session:
        flash("You're not logged in")
        return redirect("/")
    print(request.form)
    query = "INSERT INTO messages (context, created_at, updated_at, sender_id, receiver_id) VALUES (%(c)s, NOW(), NOW(), %(s_id)s, %(r_id)s);"
    data = {
        'c': request.form["context"],
        's_id': session['user_id'],
        'r_id': request.form['receiver_id']
    }
    mysql = connectToMySQL("login_and_registration")
    mysql.query_db(query, data)
    return redirect("/wall")


@app.route("/messages/<id>/destroy")
def delete_message(id):
    if not 'user_id' in session:
        flash("You're not logged in")
        return redirect("/")
    query = "DELETE FROM messages WHERE id = %(id)s;"
    data = {
        "id": id
    }
    mysql = connectToMySQL("login_and_registration")
    mysql.query_db(query, data)
    return redirect("/wall")


@app.route("/success")
def success():
    if not 'user_id' in session:
        return redirect("/")
    return render_template("success.html")


@app.route("/logout")
def logout():
    if not 'user_id' in session:
        flash("You're not logged in")
        return redirect("/")
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

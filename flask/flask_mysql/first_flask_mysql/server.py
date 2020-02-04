from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'BCBCBC'

@app.route('/')
def index():
    mysql = connectToMySQL("first_flask")
    friends = mysql.query_db("SELECT * FROM friends;")
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    is_valid = True
    if len(request.form['fname']) < 1:
        is_valid = False
        flash("Please enter a first name")
    if len(request.form['lname']) < 1:
        is_valid = False
        flash("Please enter a last name")
    if len(request.form['occ']) < 2:
        is_valid = False
        flash("Occupation should be at least 2 characters")
    
    if not is_valid:
        return redirect("/")
    else:
    # add user to database
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(oc)s, NOW(), NOW());"
        data = {
            "fn": request.form["fname"],
            "ln": request.form["lname"],
            "oc": request.form["occ"]}
        db = connectToMySQL('first_flask')
        db.query_db(query, data)
        flash("Friend successfully added!")
        return redirect("/")    # eventually we may have a different success route

if __name__ == "__main__":
    app.run(debug=True)

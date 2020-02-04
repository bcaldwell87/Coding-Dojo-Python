from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/users')
def index():
    mysql = connectToMySQL("users_flask")
    users = mysql.query_db("SELECT * FROM users;")
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/users/new")
def new_user_page():
    return render_template("createnewuser.html")

@app.route("/users/create", methods=["POST"])
def add_user_to_db():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"]
    }
    db = connectToMySQL('users_flask')
    user_id = db.query_db(query, data)  
    return redirect("/users/"+str(user_id))

@app.route("/users/<user_id>")
def user(user_id):
    id_as_int=int(user_id)
    query_string = "SELECT * FROM users WHERE user_id=%(id)s"
    data = {'id': id_as_int}
    print(id_as_int)
    userList = connectToMySQL('users_flask')
    result= userList.query_db(query_string, data)
    print(result[0])

    return render_template('viewuser.html', user=result[0])

@app.route("/users/<user_id>/edit")
def edit_user(user_id):
    id_as_int=int(user_id)
    query_string = "SELECT * FROM users WHERE user_id=%(id)s"
    data = {'id': id_as_int}
    print(id_as_int)
    userList = connectToMySQL('users_flask')
    result= userList.query_db(query_string, data)
    print(result[0])

    return render_template('edituser.html', user=result[0])

@app.route("/users/update", methods=["POST"])
def update_user_to_db():
    query = "UPDATE users SET first_name=%(fn)s, last_name=%(ln)s, email=%(em)s, updated_at= NOW() WHERE user_id=%(id)s;"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"],
        "id": request.form["user_id"]
    }
    db = connectToMySQL('users_flask')
    db.query_db(query, data)    
    return redirect("/users/"+request.form["user_id"])

@app.route("/users/<user_id>/destroy", methods=['get'])
def delete(user_id):
    query = "DELETE FROM users WHERE user_id=%(id)s;"
    data = {'id': user_id,}
    db = connectToMySQL('users_flask')
    db.query_db(query, data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)


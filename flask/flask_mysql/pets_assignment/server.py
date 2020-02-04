from flask import Flask, render_template, request, redirect
from petssqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL("pets_flask_project")
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/create_pet", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(n)s, %(ty)s, NOW(), NOW());"
    data = {
        "n": request.form["name"],
        "ty": request.form["type"]
    }
    db = connectToMySQL('pets_flask_project')
    db.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

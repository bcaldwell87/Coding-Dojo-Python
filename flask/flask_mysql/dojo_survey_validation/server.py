from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'BCBCBC'

@app.route('/')
def index():
    mysql = connectToMySQL("dojo_survey")
    survey = mysql.query_db("SELECT * FROM survey;")
    print(survey)
    return render_template("index.html", all_surveys = survey)

@app.route('/result', methods=['POST'])
def create_user():
    is_valid = True
    if len(request.form['name']) < 1:
        is_valid = False
        flash("Please enter a valid name")
    if len(request.form['location']) < 1:
        is_valid = False
        flash("Please enter a valid location")
    if len(request.form['language']) < 1:
        is_valid = False
        flash("Please enter a valid language")
    if len(request.form['comments']) < 1:
        is_valid = False
        flash("Please enter some comments")
    
    if not is_valid:
        return redirect("/")
    else: 
        flash("Friend successfully added!")
        return redirect("/")

    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comments_from_form = request.form['comments']
    return render_template("show.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, comments_on_template=comments_from_form)

if __name__ == "__main__":
    app.run(debug=True)

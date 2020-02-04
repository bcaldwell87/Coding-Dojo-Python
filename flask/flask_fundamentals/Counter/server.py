from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'BlakeCaldwell'

@app.route("/")
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  
    else:
        session['visits'] = 1 
    return "Visit Counter: {}".format(session.get('visits'))

@app.route('/destroy_session')
def delete_visits():
    session.clear()
    session.pop('visits', None)
    return 'Visits deleted'

if __name__=="__main__":
    app.run(debug=True)

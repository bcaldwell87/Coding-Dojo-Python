from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojdddddo!'

# @app.route('/say/<name>')
# def hello(name):
#     print(name)
#     return "Hi " + name +"!"

@app.route('/repeat/<num>/<whatever>')
def name(num, whatever):
    print(whatever)
    return whatever  *  int(num)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
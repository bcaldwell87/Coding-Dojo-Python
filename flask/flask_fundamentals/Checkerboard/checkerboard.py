from flask import Flask, render_template
import math
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<rows>")
def custom(rows):
    rows = int(rows)
    if rows % 2 == 0:
        odd = False
        rows = rows/2
    else:
        odd = True
        rows = math.floor(rows/2)
    return render_template("custom.html", num_rows=int(rows), odd=odd)

if __name__ == "__main__":
    app.run(debug=True)
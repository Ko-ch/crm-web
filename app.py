from flask import Flask, render_template

from db import db

app = Flask(__name__)


@app.route("/index")
def index():
    customers = db()
    return render_template("index.html", customers=customers)


@app.route("/add")
def add():
    customer = addcustomer()


if __name__ == "__main__":
    app.run(debug=True)

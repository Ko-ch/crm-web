from flask import Flask, render_template, request
from werkzeug.utils import redirect

from db import db, addcustomer

app = Flask(__name__)


@app.route("/index")
def index():
    customers = db()
    return render_template("index.html", customers=customers)


@app.route("/add", methods=['POST'])
def add():
    """
    データベースに取得したデータを保存するアプリ
    """
    name = request.form["name"]
    age = request.form["age"]
    addcustomer(name, age)
    return redirect("/index")


if __name__ == "__main__":
    app.run(debug=True)

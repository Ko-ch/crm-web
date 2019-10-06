from flask import Flask, render_template

app = Flask(__name__)

"""
コーディング内容
    /index で GET リクエストがきたら
    index.html というテンプレートをレンダリングする
"""


@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

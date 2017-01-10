from flask import Flask, render_template,  request
import os

app = Flask(__name__)
app.secret_key = "ABC"


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/process', methods=['POST'])
def process():
    print "Here"
    name = request.form.get("name")
    print name
    return render_template("view.html", name=name)

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)


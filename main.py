from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is the main page <h3> Hello! </h3>"

@app.route("/products")
def products():
    return "Hello, this is the <h3> Products! </h3> page!"

@app.route("/contactus")
def contactUs():
    return "Hello, this is the <h3> Contact Us! </h3> page!"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
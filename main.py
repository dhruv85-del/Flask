from flask import Flask,render_template

app = Flask(__name__, static_folder="static")

#URL =>end point /=> root
@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/handle-login", methods=["POST","GET"])
def handle_login():
    return "login successful"

app.run(debug=True)# run the code
from flask import Flask,render_template,url_for,request

app = Flask(__name__, static_folder="static")

#URL =>end point /=> root
@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
          name=request.form["username"]
          password=request.form["password"]
          return f"<p>Welcome {name}<P>"
    else:
        return render_template("login.html")

  

app.run(debug=True)# run the code
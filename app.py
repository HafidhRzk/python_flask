from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "token"

@app.route("/")
def base():
    return "Your Flask App Running in localhost:5000, Go to <a href='/index'>Index</a> Page"

@app.route("/index")
def index(): 
    samplesttr = "Ini String"
    sampleint = 120
    samplearr = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    sampleif = "bukan"
    return render_template("index.html", str = samplesttr, int = sampleint, arr = samplearr, ifsamp = sampleif)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/details/<value>")
def details(value):
    # return render_template("details.html").format(value)
    return "Ini id = {}, Go to <a href='/index'>Index</a> Page".format(value)

@app.route("/params")
def params():
    data = request.args.get("querystring")
    return "Ini param = {}, Go to <a href='/index'>Index</a> Page".format(data)

if __name__ == "__main__":
    app.run(debug=True)
# end main
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
# end main
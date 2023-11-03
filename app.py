from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index(): 
    samplesttr = "Ini String"
    sampleint = 120
    samplearr = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    sampleif = "bukan"
    return render_template("index.html", str = samplesttr, int = sampleint, arr = samplearr, ifsamp = sampleif)

if __name__ == "__main__":
    app.run(debug=True)
# end main
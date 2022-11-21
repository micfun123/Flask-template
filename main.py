from flask import Flask , render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

#404 error (page not founds)
@app.errorhandler(404)
def page_not_found(e):
    return str(e)

#redirect to a different site
@app.route("/redirect")
def redirect_to_google():
    return redirect("https://www.google.com")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=80)
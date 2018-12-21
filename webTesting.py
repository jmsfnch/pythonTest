from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html',title="this is the title")


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


### When lauched from the command line, the script is run in debug mode
if __name__ == '__main__':
    app.run(debug=True)

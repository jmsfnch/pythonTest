from flask import Flask, render_template
app = Flask(__name__)

siteName="Python Test"

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html',title=siteName+" - Home")


@app.route("/about")
def about():
    return render_template('about.html',title=siteName+" - About")


### When lauched from the command line, the script is run in debug mode
if __name__ == '__main__':
    app.run(debug=True)

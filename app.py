from flask import Flask,render_template

app = Flask(__name__)
app.app_context().push()

@app.route("/")
def home():
    return render_template('DHomePage.html')

@app.route("/tasks")
def tasks():
    return render_template('commits.html')

@app.route("/ptasks")
def ptasks():
    return render_template('tasks.html')

@app.route("/newcommit")
def newcommit():
    return render_template('newcommit.html')


if __name__ == "__main__":
    app.run(debug=True)


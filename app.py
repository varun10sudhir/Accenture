from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from forms import TaskForm,NewCommit
import os


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///main.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')

class Todo(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    todo = db.Column(db.String(length=100),nullable=False)

@app.route("/")
def home():
    return render_template('DHomePage.html')

@app.route("/tasks")
def tasks():
    return render_template('ttasks.html')

@app.route("/ptasks",methods=['POST','GET'])
def ptasks():
    form = TaskForm()
    if form.validate_on_submit():
        new_todo = Todo(todo = form.todo.data)
        db.session.add(new_todo)
        db.session.commit()
    todos = Todo.query.filter_by()
    return render_template('ptasks.html',form=form,todos=todos)

@app.route("/newcommit")
def newcommit():
    form = NewCommit()
    return render_template('new.html',form=form)

@app.route("/commit")
def commit():
    return render_template("commit.html")


if __name__ == "__main__":
    app.run(debug=True,port=8001)


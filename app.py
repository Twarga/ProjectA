from flask import Flask , render_template , request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# /// = relative path , //// = absolute path 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def home():
    todo_list = Todo.query.all()


@app.route("/add" , methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title , complete=False)
    db.session.add(new_todo)
    db.session.commit()




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marks.db'
db = SQLAlchemy(app)


class Marks(db.Model):
	__tablename__ = 'table_marks'
	name = db.Column('name',db.String, primary_key=True)
	subject = db.Column('subject',db.String)
	marks = db.Column('marks',db.Integer)

	def __init__(self,name,subject,marks):
		self.name = name
		self.subject = subject
		self.marks = marks



@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
	if request.method == 'POST':
		name = request.form['name']
		subject = request.form['subject']
		marks = request.form['marks']

	new_record = Marks(name,subject,marks)
	db.session.add(new_record)
	db.session.commit()

	return render_template('complete.html')


if __name__ == "__main__":
    app.run()
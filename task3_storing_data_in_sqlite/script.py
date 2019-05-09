import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
	if request.method == 'POST':
		name = request.form['name']
		subject = request.form['subject']
		marks = request.form['marks']

	# fo = open("marks.txt", "a")
	# fo.writelines(name)
	# fo.writelines(' ')
	# fo.writelines(subject)
	# fo.writelines(' ')
	# fo.writelines(marks)
	# fo.writelines('\n')
	# fo.close()
	conn = sqlite3.connect('database.db')
	c=conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS marks (name TEXT, subject TEXT, marks INTEGER)')
	c.execute('INSERT INTO marks (name, subject, marks) VALUES (?, ?, ?)',
		(name,subject,marks))
	conn.commit()
	c.close()
	conn.close()
	return render_template('complete.html')


if __name__ == "__main__":
    app.run()
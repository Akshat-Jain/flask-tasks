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

	try:
	   val = int(marks)
	   print("Yes, valid marks have been entered.")
	except ValueError:
	   print("That's not an integer!")

	fo = open("marks.txt", "a")
	fo.writelines(name)
	fo.writelines(' ')
	fo.writelines(subject)
	fo.writelines(' ')
	fo.writelines(marks)
	fo.writelines('\n')
	fo.close()

	return render_template('complete.html')


if __name__ == "__main__":
    app.run()
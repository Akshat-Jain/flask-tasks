import os
from flask import Flask, request, send_from_directory, request, render_template

app = Flask(__name__, static_url_path='/')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# APP_ROOT = /Users/akshatjain.ext/Downloads/flask_tutorial

# @app.route('/')
# def home_page():
# 	return "Welcome."


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.route('/')
def index():
	return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	target = os.path.join(APP_ROOT, 'images/')
	print(target)

	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist('file'):
		print(file)
		filename = file.filename
		destination = '/'.join([target,filename])
		print(destination)
		file.save(destination)

	return render_template('complete.html')


if __name__ == "__main__":
    app.run()


# DRY - Don't repeat yourself
# Unittest
# SQLAlchemy
# Blueprint











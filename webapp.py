from flask import Flask, render_template, redirect, url_for, request
from backend import be_worker

app = Flask(__name__)



@app.route('/')
@app.route('/home', methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET'])
def login_page():
	return render_template("login_page.html")

@app.route('/log_in', methods=['POST'])
def log_in():
	login_text = request.form['login']
	password_text = request.form['password']
	print("{}:{}".format(login_text, password_text))

	if be_worker.login_password_verification(login_text, password_text):
		return redirect(url_for('base'))
	else:
		return redirect(url_for('error'))


@app.route('/base', methods=['GET'])
def base():
	return render_template("base.html")


@app.route('/error', methods=['GET'])
def error():
	return render_template("error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
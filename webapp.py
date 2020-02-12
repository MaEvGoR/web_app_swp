from flask import Flask, render_template, redirect, url_for, request
from database import db_worker

app = Flask(__name__)



@app.route('/')
@app.route('/home', methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET'])
def login_page():
	return render_template("login_page.html", login_ins=db_worker.get_last_requests())

@app.route('/log_in', methods=['POST'])
def log_in():
	login_text = request.form['login']
	password_text = request.form['password']
	print("{}:{}".format(login_text, password_text))
	db_worker.add_request()

	return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
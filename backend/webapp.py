from flask import Flask, render_template, redirect, url_for, request
from backend import be_worker

app = Flask(__name__)

# Temporary for CORS. Should not be needed with Docker (when both apps are on same origin)
@app.after_request
def allow_cors(response):
	response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
	response.headers['Access-Control-Allow-Headers'] = 'content-type'
	return response

@app.route('/')
@app.route('/home', methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/login', methods=['GET'])
def login_page():
	return render_template("login_page.html")

@app.route('/log_in', methods=['POST'])
def log_in():
	email_text = request.json['email']
	password_text = request.json['password']

	if be_worker.login_password_verification(email_text, password_text):
		return jsonify({'name': 'rufina', 'email': 'r.talalaeva@innopolis.university'})
	else:
		abort(401)


@app.route('/base', methods=['GET'])
def base():
	return render_template("base.html")


@app.route('/error', methods=['GET'])
def error():
	return render_template("error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
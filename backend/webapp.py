from flask import Flask, render_template, redirect, url_for, request, Blueprint, jsonify
from backend.views import api

# все равно юзаем пострескл, нада уже заимпортить все по красоте
# from backend.be_worker import login_password_verification

app = Flask(__name__)

# Temporary for CORS. Should not be needed with Docker (when both apps are on same origin)
# @app.after_request
# def allow_cors(response):
# 	response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
# 	response.headers['Access-Control-Allow-Headers'] = 'content-type'
# 	return response

# @app.route('/')
# @app.route('/home', methods=['GET'])
# def home():
# 	return render_template('home.html')

# @app.route('/login', methods=['GET'])
# def login_page():
# 	return render_template("login_page.html")


# @app.route('/base', methods=['GET'])
# def base():
# 	return render_template("base.html")


# @app.route('/error', methods=['GET'])
# def error():
# 	return render_template("error.html")


app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
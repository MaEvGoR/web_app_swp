from flask import Flask, render_template, redirect, url_for, request, Blueprint, jsonify
from backend.views import api

# все равно юзаем пострескл, нада уже заимпортить все по красоте
# from backend.be_worker import login_password_verification

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

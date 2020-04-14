from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')

# Until migration to postgres
def login_password_verification(email, password):
	return True


@api.route('/example')
def example():
	return jsonify({'data': 'something'})


@api.route('/log_in', methods=['POST'])
def log_in():
	if not request.is_json:
		abort(400)
	email_text = request.json.get('email')
	password_text = request.json.get('password')

	if not login_password_verification(email_text, password_text):
		abort(401)

	return jsonify({
		'name': 'rufina',
		'email': 'r.talalaeva@innopolis.university',
	})

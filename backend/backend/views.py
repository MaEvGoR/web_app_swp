from flask import Blueprint, jsonify, request, abort
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

	status = ''
	if email_text[-3:] == '.ru':
		status = 'doe'
	else:
		status = 'student'

	return jsonify({
		'name': 'rufina',
		'email': 'r.talalaeva@innopolis.university',
		'status': status,
	})

@api.route('/new_survey', methods=['POST'])
def new_survey():
	if not request.is_json:
		abort(400)
	survey_name = request.json.get('surveyName')
	questions = request.json.get('questions')

	return jsonify({
		'survey': survey_name,
	})

@api.route('/submit_survey', methods=['POST'])
def submit_survey():
	if not request.is_json:
		abort(400)
	survey_name = request.json.get('surveyName')
	questions = request.json.get('answers')
	# answers = []
	# for i in questions:
	# 	answers.append(i.answer)

	return jsonify({
		'answers': questions
	})

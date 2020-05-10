from flask import Blueprint, jsonify, request, abort

from database import db_worker


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/example')
def example():
	return jsonify({'data': 'something'})


@api.route('/log_in', methods=['POST'])
def log_in():
	if not request.is_json:
		abort(400)
	email_text = request.json.get('email')
	password_text = request.json.get('password')

	res = db_worker.check_login_password(email_text, password_text)

	if 'error' in res.keys():
		abort(401)

	return jsonify(res)

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

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


@api.route('/student_page', methods=['POST'])
def student_page():
    if not request.is_json:
        abort(400)

    user_id = request.json.get('_id')
    student_unfilled_courses = db_worker.get_student_unfilled_courses(user_id)

    return jsonify({'courses': [{'name': course} for course in student_unfilled_courses]})


@api.route('/surveys_page', methods=['POST'])
def surveys_page():
    if not request.is_json:
        abort(400)

    user_id = request.json.get('_id')
    req_course = request.json.get('course')
    unfilled_surveys = db_worker.get_student_unfilled_surveys(user_id, req_course)

    return jsonify({'course': req_course, 'surveys': unfilled_surveys})


@api.route('/bs_years', methods=['GET'])
def get_years():
    return jsonify(db_worker.get_all_years())


@api.route('/courses', methods=['POST'])
def get_courses():
    if not request.is_json:
        abort(400)

    req_year = request.json.get('year')
    return jsonify(db_worker.get_courses(req_year))


@api.route('/new_survey', methods=['POST'])
def new_survey():
    if not request.is_json:
        abort(400)

    year = request.json.get('year')
    course_id = request.json.get('course_id')
    user_id = request.json.get('user_id')
    survey_title = request.json.get('title')
    questions = request.json.get('questions')

    res = db_worker.create_new_survey(year, course_id, user_id, survey_title, questions)

    return jsonify(res)


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

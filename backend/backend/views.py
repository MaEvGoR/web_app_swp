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

    return jsonify(
        {'courses': [{'name': course['name'], 'course_id': course['_id']} for course in student_unfilled_courses]})


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


@api.route('/survey', methods=['POST'])
def get_survey():
    if not request.is_json:
        abort(400)

    survey_name = request.json.get('survey_name')
    survey_id = request.json.get('survey_id')
    user_id = request.json.get('_id')

    not_passed_questions = db_worker.get_unfilled_questions(user_id, survey_id)

    return jsonify({"survey_id": survey_id, "name": survey_name, "questions": not_passed_questions})


@api.route('/submit_survey', methods=['POST'])
def submit_survey():
    if not request.is_json:
        abort(400)

    user_id = request.json.get('user_id')
    survey_id = request.json.get('survey_id')
    course_id = request.json.get('course_id')
    questions = request.json.get('answers')

    res = db_worker.save_answers(user_id, survey_id, course_id, questions)

    return jsonify(res)


@api.route('/get_surveys_by_course', methods=['POST'])
def get_surveys_by_course():
    if not request.is_json:
        abort(400)

    course_id = request.json.get('course_id')

    res = db_worker.get_all_surveys(course_id)

    return jsonify(res)



@api.route('/get_results', methods=['POST'])
def get_results():
    if not request.is_json:
        abort(400)

    survey_id = request.json.get('survey_id')
    res = db_worker.get_results(survey_id)

    return jsonify(res)

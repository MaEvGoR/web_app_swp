from flask import Blueprint, jsonify, request, abort
from database import db_worker

api = Blueprint('api', __name__, url_prefix='/api')


# Until migration to postgres
def login_password_verification(email, password):
    return True


# we assume that this is Maxim Evgrafov
current_student_id = "5e8e662b41e24db0156a0a41"


@api.after_request
def allow_cors(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://0.0.0.0:8080'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response


@api.route('/student', methods=['GET'])
def student():
    # should return
    # Name
    # unfilled surveys names (courses names)

    student_info = db_worker.get_student_info(current_student_id)
    student_unfilled_courses = db_worker.get_student_unfilled_courses(current_student_id)

    return jsonify({'name': student_info['fname'], 'unfilled_courses': student_unfilled_courses})


@api.route('/student_unfilled', methods=['POST'])
def student_unfilled():
    if not request.is_json:
        abort(400)

    required_course = request.json.get('course')
    unfilled_surveys = db_worker.get_student_unfilled_surveys(current_student_id, required_course)

    return jsonify({'course': required_course, 'surveys': unfilled_surveys})


@api.route('/log_in', methods=['POST'])
def log_in():
    if not request.is_json:
        abort(400)
    email_text = request.json.get('email')
    password_text = request.json.get('password')

    if not login_password_verification(email_text, password_text):
        abort(401)

    return jsonify({
        'name': 'maxim',
        'email': 'r.talalaeva@innopolis.university',
        'status': 'student',
    })

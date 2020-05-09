from flask import Blueprint, jsonify, request, abort
from database import db_worker

api = Blueprint('api', __name__, url_prefix='/api')


# Until migration to postgres
def login_password_verification(email, password):
    return True


# we assume that this is Maxim Evgrafov
current_id = "5e8e662b41e24db0156a0a41"


@api.route('/student', methods=['GET'])
def student():
    # should return
    # Name
    # unfilled surveys names (courses names)

    student_info = db_worker.get_student_info(current_id)
    student_unfilled_courses = db_worker.get_student_surveys(current_id)

    return {'name': student_info['fname'], 'unfilled_courses': student_unfilled_courses}


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

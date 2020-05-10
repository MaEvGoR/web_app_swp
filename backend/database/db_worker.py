import pymongo
import dns
from faker import Faker
import datetime
from bson.objectid import ObjectId

fake = Faker()

client = pymongo.MongoClient(
    "mongodb+srv://admin:feedbackadmin@firstcluster-nk57p.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

students = db['students']
courses = db['courses']
doe = db['doe']
surveys = db['surveys']
questions = db['questions']
answers = db['answers']


def get_student_info(student_id):
    # return student document from database

    query = list(students.find({'_id': ObjectId(student_id)}))
    return query[0]


def get_survey_info(survey_id):
    # return survey document from database

    query = list(surveys.find({'_id': ObjectId(survey_id)}))
    return query[0]


def get_question_info(question_id):
    query = list(questions.find({'_id': question_id}))

    changed = query[0]
    changed['_id'] = str(changed['_id'])
    return changed


def course_from_survey(survey_id):
    # return course where this survey id is

    query = list(courses.find({"survey_ids": survey_id}))
    return query[0]


def get_all_courses():
    query = list(courses.find({}))
    return [{'name': course['name'], '_id': str(course['_id'])} for course in query]


def get_all_years():
    query = list(courses.find({}))
    years = set()
    for course in query:
        years.add(course['year'])

    return [{'year': year} for year in years]


def get_student_courses(student_id):
    # return list of courses of student

    student = get_student_info(student_id)

    student_year = int(student['start_year'])

    student_courses = list(courses.find({'year': student_year}))
    return student_courses


def get_student_surveys_ids(student_id):
    # return ids of ALL surveys of student
    student_courses = get_student_courses(student_id)
    student_surveys_ids = []

    for course in student_courses:
        student_surveys_ids += course['survey_ids']

    return student_surveys_ids


def get_question_ids_of_survey(survey_id):
    # return ids of questions in survey

    survey_info = get_survey_info(survey_id)
    return survey_info['questions']


def num_of_empty_answers(student_id, survey_id):
    # return number of unanswered questions in specific
    # survey for specific student

    survey_questions = get_question_ids_of_survey(survey_id)
    questions_num = len(survey_questions)

    for question in survey_questions:
        query = list(answers.find({"student_id": ObjectId(student_id),
                                   "survey_id": survey_id,
                                   "question_id": question}))

        if len(query) != 0:
            questions_num -= 1

    return questions_num


def get_student_unfilled_courses(student_id):
    # return info about surveys that are not passed yet

    student_surveys = get_student_surveys_ids(student_id)

    unfilled_surveys_courses = set()
    for survey_id in student_surveys:

        # todo date checking!!!

        if num_of_empty_answers(student_id, survey_id) != 0:
            unfilled_surveys_courses.add(course_from_survey(survey_id)['name'])

    return list(unfilled_surveys_courses)


def get_student_unfilled_surveys(student_id, req_course):
    # return unfilled surveys of the specific course

    student_surveys = get_student_surveys_ids(student_id)
    unfilled_surveys = []
    for survey_id in student_surveys:

        # todo date checking!!!

        if num_of_empty_answers(student_id, survey_id) != 0 and course_from_survey(survey_id)['name'] == req_course:
            unfilled_surveys.append({'name': get_survey_info(survey_id)['name'],
                                     '_id': str(survey_id)})

    return unfilled_surveys


def get_unfilled_questions(student_id, survey_id):
    # return info about questions

    survey_questions = get_question_ids_of_survey(survey_id)

    questions = []

    for question in survey_questions:
        query = list(answers.find({"student_id": ObjectId(student_id),
                                   "survey_id": ObjectId(survey_id),
                                   "question_id": question}))

        if len(query) == 0:
            questions.append(get_question_info(question))

    return questions


# print(get_unfilled_questions("5e8e662b41e24db0156a0a41", "5eb71774703d82a2afce21e8"))
# exit(0)


# print(get_student_unfilled_surveys("5e8e662b41e24db0156a0a41"))
# exit(0)

def check_login_password(email, password):
    query_result = list(students.find({'email': email, 'password': password}))

    if len(query_result) != 0:
        return_state = {'email': email,
                        'name': query_result[0]['fname'],
                        'status': 'student',
                        '_id': str(query_result[0]['_id'])}

        return return_state

    query_result = list(doe.find({'email': email, 'password': password}))
    if len(query_result) != 0:
        return_state = {'email': email,
                        'name': query_result[0]['fname'],
                        'status': 'doe',
                        '_id': str(query_result[0]['_id'])}

        return return_state

    return {'error': 401}

# def check_login_password(email, password):
#     query_result = list(students.find({'email': email, 'password': password}))
#     return query_result

# for course in list(courses.find({})):
#     courses.update_one({'_id': course['_id']}, {'$set': {'survey_ids': []}})

# surveys_info = []

# for course in list(courses.find({})):
#     surveys_amount = fake.random_int(min=0, max=2)
#
#     for i in range(surveys_amount):
#         name = fake.random_choices(elements=('Current Course Feedback', 'Last Lecture Feedback',
#                                              'Quality of course', 'Feedback to Professor'), length=1)[0]
#
#         start_date = fake.date_between_dates(date_start=datetime.date(2020, 5, 4), date_end=datetime.date(2020, 5, 10))
#         end_date = fake.date_between_dates(date_start=datetime.date(2020, 5, 15), date_end=datetime.date(2020, 5, 20))
#
#         # print(str(start_date))
#         #
#         # creation_time = datetime.datetime.timestamp(start_date)
#         # expiration_time = datetime.datetime.timestamp(end_date)
#
#         description = fake.text()
#
#         mongo_surv = surveys.insert_one({'name': name,
#                                          'creation_time': str(start_date),
#                                          'expiration_time': str(end_date),
#                                          'description': description,
#                                          'created_by': "5eb70b92f58a3003a2d4a292",
#                                          'questions': []})
#
#         courses.update_one({'_id': course['_id']},
#                            {'$push': {'survey_ids': mongo_surv.inserted_id}})

# print('hui')


# for survey in list(surveys.find({})):
#     mongo_question = questions.insert_one({'text': 'Put your number here:',
#                                            'q_num': 0,
#                                            'type': 0})
#
#     surveys.update_one({'_id': survey['_id']},
#                        {'$push': {'questions': mongo_question.inserted_id}})
#
# print('hui')


# doe = db['doe']
#
# doe_info = []
#
# for _ in range(5):
#     fname = fake.first_name()
#     lname = fake.last_name()
#
#     email = fake.ascii_free_email()
#     password = fake.word()
#
#     doe_info.append({'fname': fname,
#                      'lname': lname,
#                      'email': email,
#                      'password': password})
#
# doe_info.append({'fname': 'Maxim',
#                  'lname': 'Evgrafov',
#                  'email': 'doe@innopolis.university',
#                  'password': 'maximevgrafovdoe'})
#
# doe.insert_many(doe_info)

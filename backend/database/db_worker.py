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


def get_courses(year):
    query = list(courses.find({'year': year}))
    return [{'name': course['name'], '_id': str(course['_id'])} for course in query]

def get_all_surveys(course_id):
    survey_ids_by_course = list(courses.find({'_id': ObjectId(course_id)}))[0]['survey_ids']

    surveys_objects = []
    for survey_id in survey_ids_by_course:
        survey_obj = list(surveys.find({'_id': survey_id}))[0]
        surveys_objects.append({'name':survey_obj['name'], '_id': str(survey_id)})

    return surveys_objects






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

    unfilled_surveys_courses = []
    for survey_id in student_surveys:

        # todo date checking!!!

        if num_of_empty_answers(student_id, survey_id) != 0:
            flag = 0
            for i in range(len(unfilled_surveys_courses)):
                if unfilled_surveys_courses[i]['_id'] == str(course_from_survey(survey_id)['_id']):
                    flag += 1

            if flag == 0:
                unfilled_surveys_courses.append({'name': course_from_survey(survey_id)['name'],
                                                 '_id': str(course_from_survey(survey_id)['_id'])})

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
        return_state = {'status': 'student',
                        '_id': str(query_result[0]['_id'])}

        return return_state

    query_result = list(doe.find({'email': email, 'password': password}))
    if len(query_result) != 0:
        return_state = {'status': 'doe',
                        '_id': str(query_result[0]['_id'])}

        return return_state

    return {'error': 401}


def create_new_survey(year, course_id, doe_id, title, n_questions):
    # year: 17-19
    # course_id: 123jh1k2j3hkshgrk32
    # questions: [
    #     {title: "What you don\'t like about the course?", type: 'text'},
    #     {title: "Content of the course?", type: 'radio', options: ['Excellent', 'Good', 'Satisfactory', 'Very bad']},
    # ],

    question_ids = []

    for i in range(len(n_questions)):
        q_object = {'text': n_questions[i]['title'],
                    'q_num': i,
                    'type': n_questions[i]['type']}

        if q_object['type'] == 'radio':
            q_object['options_flag'] = True
            q_object['options'] = n_questions[i]['options']

        res_q = questions.insert_one(q_object)
        question_ids.append(res_q.inserted_id)

    survey_object = {'name': title,
                     'creation_time': str(datetime.date(datetime.datetime.today().year,
                                                        datetime.datetime.today().month,
                                                        datetime.datetime.today().day)),
                     'expiration_time': str(datetime.date(datetime.datetime.today().year,
                                                          datetime.datetime.today().month,
                                                          datetime.datetime.today().day) + datetime.timedelta(days=10)),
                     'description': fake.text(),
                     'created_by': doe_id,
                     'questions': [ObjectId(q_id) for q_id in question_ids]}

    mongo_surv = surveys.insert_one(survey_object)

    courses.update_one({'_id': ObjectId(course_id)},
                       {'$push': {'survey_ids': mongo_surv.inserted_id}})

    return {'response': 200}


def save_answers(user_id, survey_id, course_id, questions_answers):
    # {'user_id': '7bsd7fg7b3eybdv834',
    #      'survey_id': 'hsfdb82uejdvu9b29',
    #      'course_id': 'fjns019eih82b90enj',
    #      'questions': [
    #          {'question_id':'isdn29weivfh29evnd',
    #           'type': 'text',
    #           'answer': 'awesome'},
    #          {'question_id': 'idwnj192ewinjv92osig',
    #           'type': 'text',
    #           'answer': 'cool'},
    #          {'question_id': 'asudh91wncdv9328duqw',
    #           'type': 'radio',
    #           'answer': 'Excellent'}
    #      ]}

    answers_objects = []
    for raw_ans in questions_answers:
        ans_object = {'student_id': ObjectId(user_id),
                      'course_id': ObjectId(course_id),
                      'survey_id': ObjectId(survey_id),
                      'question_id': ObjectId(raw_ans['_id']),
                      'answer': raw_ans['title']}

        answers_objects.append(ans_object)

    for ans_object in answers_objects:
        # update if exists
        # insert if doesn't

        answers.update({'student_id': ans_object['student_id'],
                        'course_id': ans_object['course_id'],
                        'survey_id': ans_object['survey_id'],
                        'question_id': ans_object['question_id']},
                       ans_object,
                       True)

    return {'response': 200}


def get_results(survey_id):
    ## EXAMPLE OF RETURNED OBJECT

    # return_obj = {'_id': ObjectId(survey_id),
    #               'course_name': 'Course Name',
    #               'name': "Survey Name",
    #               'creation_time': "2020-05-07",
    #               'expiration_time': "2020-05-17",
    #               'description': 'Survey Description',
    #               'created_by': 'Creator id',
    #               'results': [
    #                   {'question_id': ObjectId('Question1_id'),
    #                    'text': 'Question1 text',
    #                    'q_num': 'Question1 number',
    #                    'type': 'Question1 type (text ot radio)',
    #                    'answers': [{'answer': 'ans1'},
    #                                {'answer': 'ans2'},
    #                                {'answer': 'ans3'}
    #                                ]},
    #                   {'question_id': ObjectId('Question2_id'),
    #                    'text': 'Question2 text',
    #                    'q_num': 'Question2 number',
    #                    'type': 'Question2 type (text ot radio)',
    #                    'answers': [{'answer': 'ans1'},
    #                                {'answer': 'ans2'},
    #                                {'answer': 'ans3'}
    #                                ]}
    #               ]}

    try:
        survey_object = list(surveys.find({'_id': ObjectId(survey_id)}))[0]
    except:
        raise Exception('There is no such ({}) survey'.format(survey_id))

    return_obj = {'_id': survey_id,
                  'name': survey_object['name'],
                  'course_name': course_from_survey(ObjectId(survey_id))['name'],
                  'creation_time': survey_object['creation_time'],
                  'expiration_time': survey_object['expiration_time'],
                  'description': survey_object['description'],
                  'created_by': survey_object['created_by'],
                  'results': []}

    for question_obj_id in survey_object['questions']:
        question_result_obj = list(questions.find({'_id': question_obj_id}))[0]

        return_question_object = {'question_id': str(question_result_obj['_id']),
                                  'text': question_result_obj['text'],
                                  'q_num': question_result_obj['q_num'],
                                  'type': question_result_obj['type'],
                                  'options_flag': True if question_result_obj['type'] == 'radio' else False,
                                  'options': question_result_obj['options'] if question_result_obj[
                                                                                   'type'] == 'radio' else None,
                                  'answers': []}

        if return_question_object['options_flag']:

            for elem in return_question_object['options']:
                return_question_object['answers'].append({'option': elem, 'number': 0})

        answers_objects = list(answers.find({'question_id': ObjectId(return_question_object['question_id'])}))

        for ans_obj in answers_objects:
            if return_question_object['options_flag']:
                # count
                return_question_object['answers'][int(ans_obj['answer'])]['number'] += 1
            else:
                # just add
                return_question_object['answers'].append({'answer': ans_obj['answer']})

        return_obj['results'].append(return_question_object)

    return return_obj

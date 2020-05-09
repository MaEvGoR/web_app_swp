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


def get_student_info(student_id):
    query = list(students.find({'_id': ObjectId(student_id)}))
    return query[0]


def get_student_surveys(student_id):
    return ['C1', 'C2', 'C3']


# print(get_student_info("5e8e662b41e24db0156a0a41"))
# exit(0)

def check_login_password(email, password):
    query_result = list(students.find({'email': email, 'password': password}, {"_id": 0, 'password': 0}))
    return query_result

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

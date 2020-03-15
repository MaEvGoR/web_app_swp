# from redis import Redis

# rd = Redis(host='redis', db=0)

# def get_last_requests():
# 	return rd.get('requests')

# def add_request():
# 	rd.set('requests', int(rd.get('requests'))+1)



# test data generated manually
test_data = [
{3238:{'login':'m.evgrafov@innopolis.university','password':'0'}},
{3318:{'login':'r.talalaeva@innopolis.university','password':'1'}},
{3258:{'login':'r.muraviev@innopolis.university','password':'2'}},
{3108:{'login':'i.ishbaev@innopolis.university','password':'3'}}
]



def get_login_password_info():

	# here some actions to get data from database

	return test_data
from redis import Redis

rd = Redis(host='redis', db=0)

def get_last_requests():
	return rd.get('requests')

def add_request():
	rd.set('requests', int(rd.get('requests'))+1)
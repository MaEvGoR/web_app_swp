from database import db_worker

def hash_id_from_email(email):
	hash_int = 0

	for character in email:
		hash_int += ord(character)

	return hash_int

def login_password_verification(login, password):

	data = db_worker.get_login_password_info()

	for item in data:
		if hash_id_from_email(login) in item.keys():
			if password == item[hash_id_from_email(login)]['password']:
				return True
	return False
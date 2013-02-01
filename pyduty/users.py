import copy
from pyduty.utils import list_get_func, ListIterator, post

def get_users(key, domain, **kwargs):
	func = list_get_func(key, domain, 'api/v1/users', **kwargs)
	return ListIterator(func, 'users')

def create_user(key, domain, name, email, requester_id, **kwargs):
	data = copy.copy(kwargs)
	data['name'] = name
	data['email'] = email
	data['requester_id'] = requester_id
	return post(key, domain, 'api/v1/users', **data)
	

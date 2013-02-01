from pyduty.utils import list_get_func, ListIterator, get, post

def get_schedule(key, domain, schedule_id, **kwargs):
	return get(key, domain, 'api/v1/schedules', schedule_id, **kwargs)

def get_schedules(key, domain, **kwargs):
	func = list_get_func(key, domain, 'api/v1/schedules', **kwargs)
	return ListIterator(func, 'schedules')

def create_schedule(key, domain, **kwargs):
	return post(key, domain, 'api/v1/schedules', **kwargs)

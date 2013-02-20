from pyduty.utils import list_get_func, ListIterator, get, post, put

def get_service(key, domain, service_id, **kwargs):
	return get(key, domain, 'api/v1/services', service_id, **kwargs)

def get_services(key, domain, **kwargs):
	func = list_get_func(key, domain, 'api/v1/services', **kwargs)
	return ListIterator(func, 'services')

def create_service(key, domain, **kwargs):
	return post(key, domain, 'api/v1/services', **kwargs)

def update_service(key, domain, service_id, **kwargs):
	return put(key, domain, 'api/v1/services', service_id, **kwargs)

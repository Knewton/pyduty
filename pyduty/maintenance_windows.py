from pyduty.utils import list_get_func, ListIterator, get, post, delete, put

def get_maintenance_window(key, domain, maintenance_window_id, **kwargs):
	return get(key, domain, 'api/v1/maintenance_windows', maintenance_window_id, **kwargs)

def get_maintenance_windows(key, domain, **kwargs):
	func = list_get_func(key, domain, 'api/v1/maintenance_windows', **kwargs)
	return ListIterator(func, 'maintenance_windows')

def create_maintenance_window(key, domain, **kwargs):
	return post(key, domain, 'api/v1/maintenance_windows', **kwargs)

def update_maintenance_window(key, domain, maintenance_window_id, **kwargs):
	return put(key, domain, 'api/v1/maintenance_windows', maintenance_window_id, **kwargs)

def update_maintenance_window(key, domain, maintenance_window_id, **kwargs):
	return put(key, domain, 'api/v1/maintenance_windows', maintenance_window_id, **kwargs)

def delete_maintenance_window(key, domain, maintenance_window_id):
	return delete(key, domain, 'api/v1/maintenance_windows', maintenance_window_id)


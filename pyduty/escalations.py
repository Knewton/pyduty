from pyduty.utils import list_get_func, ListIterator, get, post

def get_escalation(key, domain, schedule_id, **kwargs):
	return get(key, domain, 'api/v1/escalation_policies', schedule_id, **kwargs)

def get_escalations(key, domain, **kwargs):
	func = list_get_func(key, domain, 'api/v1/escalation_policies', **kwargs)
	return ListIterator(func, 'escalation_policies')

def create_escalation(key, domain, **kwargs):
	return post(key, domain, 'api/v1/escalation_policies', **kwargs)

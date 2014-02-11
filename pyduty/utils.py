import os
import copy
import urllib
import StringIO
import json
import pycurl
import k.config

PydutyConfigPath = k.config.ConfigPathDefaults([
	'', '~/.pyduty', '/etc/pyduty'])
PydutyConfig = k.config.ConfigDefault(config_path=PydutyConfigPath)

def get_api_key(filename='api'):
	confhash = PydutyConfig.fetch_config(filename)
	try:
		return confhash['api_key']
	except:
		raise KeyError('config file has no key "api_key"')

def get_domain(filename='api'):
	confhash = PydutyConfig.fetch_config(filename)
	try:
		return confhash['domain']
	except:
		raise KeyError('config file has no key "api_key"')

def list_get_func(key, domain, path, **kwargs):
	def retfunc(offset=0):
		c = pycurl.Curl()
		body_buf = StringIO.StringIO()
		data = copy.copy(kwargs)
		data['offset'] = offset
		url = "https://%s/%s?%s" % (domain, path, urllib.urlencode(data))
		header = ['Content-type: application/json', 'Authorization: Token token=%s' % key]
		c.setopt(c.HTTPHEADER, header)
		c.setopt(c.URL, url)
		# CURL SSL CERT VERIFY OPTIONS. ADDED TD 2013.04.09
		c.setopt(pycurl.SSL_VERIFYPEER, 1)
		c.setopt(pycurl.SSL_VERIFYHOST, 2)
		c.setopt(pycurl.CAINFO, '/etc/ssl/certs/ca-certificates.crt')
		c.setopt(c.WRITEFUNCTION, body_buf.write)
		c.perform()
		jstring = body_buf.getvalue()
		return_code = c.getinfo(c.HTTP_CODE)
		if return_code != 200:
			raise Exception("Return code %s\n%s" % (return_code, jstring))
		return json.loads(jstring)
	return retfunc

class ListIterator:
	def __init__(self, func, fieldname):
		self.func = func
		self.fieldname = fieldname
		self.payload = None
		self.current = 0

	def __iter__(self):
		return self

	def next(self):
		if not self.payload:
			self.payload = self.func()
			self.current = 0
		limit = self.payload['limit']
		offset = self.payload['offset']
		total = self.payload['total']
		if self.current + offset >= total:
			raise StopIteration
		if self.current >= limit:
			newoffset = limit + offset
			self.payload = self.func(newoffset)
			self.current = 0
		self.current += 1
		return self.payload[self.fieldname][self.current - 1]

def get(key, domain, path, object_id, **kwargs):
	c = pycurl.Curl()
	body_buf = StringIO.StringIO()
	url = "https://%s/%s/%s?%s" % (domain, path, object_id, urllib.urlencode(kwargs))
	header = ['Content-type: application/json', 'Authorization: Token token=%s' % key]
	c.setopt(c.HTTPHEADER, header)
	c.setopt(c.URL, url)
	c.setopt(c.WRITEFUNCTION, body_buf.write)
	c.setopt(c.TIMEOUT, 10)
	c.perform()
	jstring = body_buf.getvalue()
	return_code = c.getinfo(c.HTTP_CODE)
	if return_code != 200:
		raise Exception("Return code %s\n%s" % (return_code, jstring))
	return json.loads(jstring)

def get_no_id(key, domain, path, **kwargs):
	c = pycurl.Curl()
	body_buf = StringIO.StringIO()
	url = "https://%s/%s?%s" % (domain, path, urllib.urlencode(kwargs))
	header = ['Content-type: application/json', 'Authorization: Token token=%s' % key]
	c.setopt(c.HTTPHEADER, header)
	c.setopt(c.URL, url)
	c.setopt(c.WRITEFUNCTION, body_buf.write)
	c.setopt(c.TIMEOUT, 10)
	c.perform()
	jstring = body_buf.getvalue()
	return_code = c.getinfo(c.HTTP_CODE)
	if return_code != 200:
		raise Exception("Return code %s\n%s" % (return_code, jstring))
	return json.loads(jstring)

def post(key, domain, path, **kwargs):
	c = pycurl.Curl()
	body_buf = StringIO.StringIO()
	url = "https://%s/%s" % (domain, path)
	header = ['Content-type: application/json', 'Authorization: Token token=%s' % key]
	c.setopt(c.HTTPHEADER, header)
	c.setopt(c.URL, url)
	c.setopt(c.POSTFIELDS, json.dumps(kwargs))
	c.setopt(c.WRITEFUNCTION, body_buf.write)
	c.setopt(c.TIMEOUT, 10)
	c.perform()
	jstring = body_buf.getvalue()
	return_code = c.getinfo(c.HTTP_CODE)
	if return_code != 201:
		raise Exception("Return code %s\n%s" % (return_code, jstring))
	return json.loads(jstring)

def delete(key, domain, path, object_id):
	c = pycurl.Curl()
	url = "https://%s/%s/%s" % (domain, path, object_id)
	header = ['Content-type: application/json', 'Authorization: Token token=%s' % key]
	c.setopt(c.HTTPHEADER, header)
	c.setopt(c.URL, url)
	c.setopt(c.TIMEOUT, 10)
	c.perform()
	return_code = c.getinfo(c.HTTP_CODE)
	if return_code != 204:
		raise Exception("Return code %s" % (return_code))
	return

def test(debug_type, debug_msg):
	print "debug(%d): %s" % (debug_type, debug_msg)

def put(key, domain, path, object_id, **kwargs):
	c = pycurl.Curl()
	body_buf = StringIO.StringIO()
	url = "https://%s/%s/%s" % (domain, path, object_id)
	header = ['Content-type: application/json', 'Authorization: Token token=%s' % key]
	c.setopt(c.PUT, 1)
	c.setopt(c.HTTPHEADER, header)
	c.setopt(c.URL, url)
	put_buf = StringIO.StringIO()
	json.dump(kwargs, put_buf)
	put_buf.seek(0)
	c.setopt(c.READFUNCTION, put_buf.read)
	c.setopt(c.INFILESIZE, put_buf.len)
	c.setopt(c.TIMEOUT, 10)
	c.setopt(c.WRITEFUNCTION, body_buf.write)
	c.perform()
	jstring = body_buf.getvalue()
	return_code = c.getinfo(c.HTTP_CODE)
	if return_code != 200:
		raise Exception("Return code %s\n%s" % (return_code, jstring))
	return json.loads(jstring)

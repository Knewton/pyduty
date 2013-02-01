#!/usr/bin/env python
import os.path
import re
from setuptools import find_packages, setup

def parse_requirements(file_name):
	"""Taken from http://cburgmer.posterous.com/pip-requirementstxt-and-setuppy"""
	requirements = []
	for line in open(os.path.join(os.path.dirname(__file__), "config", file_name), "r"):
		line = line.strip()
		# comments and blank lines
		if re.match(r"(^#)|(^$)", line):
			continue
		requirements.append(line)
	return requirements

setup(
	name="pyduty",
	version="0.1.1",
	url = "https://github.com/Knewton/pyduty",
	author="Devon Jones",
	author_email="devon@knewton.com",
	license = "Proprietary",
	scripts = [
		"schedule-get",
		"schedule-list",
		"service-list",
		"service-owner-schedule-create",
		"user-create",
		"user-list"],
	packages=find_packages(),
	package_data = {"config": ["requirements.txt"]},
	install_requires=parse_requirements("requirements.txt"),
	tests_require=parse_requirements("requirements.txt"),
	description = "Library for administrating PagerDuty.",
	long_description = "\n" + open("README").read(),
)


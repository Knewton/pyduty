#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
	name="pyduty",
	version="0.1.1" % get_version(),
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


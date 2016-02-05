# -*- coding: utf-8 -*-
"""
We try to keep all py.test configuration in this single file. Py.test is invoked
by tox.
"""
from __future__ import absolute_import, print_function, unicode_literals

import django
import os
import shutil
import sys

from kolibri.utils import compat

DEFAULT_KOLIBRI_TEST_HOME = os.path.abspath('.tmp_kolibri_home')

os.environ.setdefault('KOLIBRI_HOME', DEFAULT_KOLIBRI_TEST_HOME)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kolibri.deployment.default.settings.base')


def pytest_configure():
    """
    No-op called by py.test, we may implement customized global environment
    setup here.

    Here we can set special test configuration environments. But if you need
    to do something for running just a single test, write your own temporary
    settings module and do py.test -ds=my_settings
    See `py.test docs <http://pytest-django.readthedocs.org/en/latest/configuring_django.html>`_

    Calling ``settings.configure()`` will circumvent the settings module defined
    by ``DJANGO_SETTINGS_MODULE`` so we choose to go the module-based way.
    """
    if os.environ['KOLIBRI_HOME'] == DEFAULT_KOLIBRI_TEST_HOME:
        shutil.rmtree(os.environ['KOLIBRI_HOME'])
    elif os.path.exists(os.environ['KOLIBRI_HOME']):
        print("Test KOLIBRI_HOME exists: {}".format(os.environ['KOLIBRI_HOME']))
        yn = compat.input("Delete and continue? ")
        yn = yn.lower() if yn else None
        if yn == "y":
            shutil.rmtree(os.environ['KOLIBRI_HOME'])
        else:
            print("Quitting")
            sys.exit(1)

    # Load django settings stack
    django.setup()

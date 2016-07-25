========
Overview
========

Override arbitrary Django settings via environment variables.

* Free software: BSD license

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis|
        | |coveralls|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |travis| image:: https://travis-ci.org/jcushman/django-env-overrides.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/jcushman/django-env-overrides

.. |coveralls| image:: https://coveralls.io/repos/jcushman/django-env-overrides/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/jcushman/django-env-overrides

.. |version| image:: https://img.shields.io/pypi/v/django-env-overrides.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-env-overrides

.. |downloads| image:: https://img.shields.io/pypi/dm/django-env-overrides.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-env-overrides

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-env-overrides.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-env-overrides

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-env-overrides.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-env-overrides

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-env-overrides.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-env-overrides

.. end-badges

When to use this package
========================

This package lets you override any Django setting using environment variables, just by adding a couple of lines to the bottom of `settings.py`.

This is handy if:

* You have a project that is not currently configurable via environment variables, and you want to quickly adapt it to run in an environment like Heroku.

* You want to be able to quickly override settings on deployed code for debugging.

This is *not* a good idea as the primary way of configuring a complex project in production. In general you'll be happier keeping all settings in source control, and explicitly recording which settings need to be provided by environment variables using `django-environ <https://github.com/joke2k/django-environ>`_.

Installation
============

::

    pip install django-env-overrides

Documentation
=============

django-env-overrides lets you quickly adjust an existing Django app to load arbitrary settings from environment variables.
It uses `django-environ <https://github.com/joke2k/django-environ>`_ to parse settings from the environment, but allows override of arbitrary settings without specific changes to ``settings.py``.

Setup
-----

Add these lines to the end of your ``settings.py`` file:

::

    import django_env_overrides
    django_env_overrides.apply_to(globals())

Any environment variable prefixed with ``DJANGO__`` will now be imported to your settings.

Example
-------

settings.py:

::

    DEBUG = True
    MEDIA_URL = '/media/'
    DATABASES = {
        'default': {
            'ENGINE': 'sqlite3',
        }
    }
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                ]
            }
        }
    ]

    import django_env_overrides
    django_env_overrides.apply_to(globals())

Environment:

::

    DJANGO__SECRET_KEY=secret
    DJANGO__MEDIA_URL=/new_url/
    DJANGO__bool__DEBUG=False
    POSTGRES=postgres://uf07k1:wegauwhg@ec2-107-21-253-135.compute-1.amazonaws.com:5431/d8r82722
    DJANGO__db__DATABASES__default=$POSTGRES
    DJANGO__TEMPLATES__0__OPTIONS__context_processors__1='my.context.processor'

Result:

::

    DEBUG = False
    MEDIA_URL = '/new_url/'
    SECRET_KEY = 'secret'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd8r82722',
            'HOST': 'ec2-107-21-253-135.compute-1.amazonaws.com',
            'USER': 'uf07k1',
            'PASSWORD': 'wegauwhg',
            'PORT': 5431,
        }
    }
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'my.context.processor',
                ]
            }
        }
    ]

Format for environment variables
--------------------------------

The format for environment variable names is:

    <prefix>__<typecast>__<path>__<to>__<target>__<setting>

``<prefix>`` defaults to ``DJANGO``. If you want to use another prefix, use ``django_env_overrides.apply_to(globals(), prefix="MYPREFIX")``.

``<typecast>`` (optional) is any `type known to the django-environ package <https://github.com/joke2k/django-environ#supported-types>`_.
Currently the supported types are str, bool, int, float, json, list, tuple, dict, url, path, db_url, cache_url, search_url, and email_url.
See the django-environ package for usage. If ``<typecast>`` is omitted, values are set as ``str``.

``<path>__<to>__<target>__<setting>`` specifies the setting or subsetting the value should be assigned to. Path elements
are treated as array indexes if they are integers, and otherwise as dictionary keys.

Development
===========

See CONTRIBUTING.rst

========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/django-env-overrides/badge/?style=flat
    :target: https://readthedocs.org/projects/django-env-overrides
    :alt: Documentation Status

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

Override arbitrary Django settings via environment variables.

* Free software: BSD license

Installation
============

::

    pip install django-env-overrides

Documentation
=============

https://django-env-overrides.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

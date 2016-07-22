import os
import pytest

import django_env_overrides

### HELPERS ###

def set_from_environ(settings, **env):
    _real_env = os.environ
    os.environ = env
    try:
        django_env_overrides.import_environ_settings(settings)
    finally:
        os.environ = _real_env

@pytest.fixture
def settings():
    return {
        "MEDIA_URL": '/media/',
        "DATABASES": {
            'default': {
                'ENGINE': 'sqlite3',
            }
        },
        "TEMPLATES": [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'OPTIONS': {
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                    ]
                }
            }
        ]
    }

### TESTS ###

def test_new(settings):
    set_from_environ(settings,
                     DJANGO__NEW_SETTING="bar")
    assert settings.get('NEW_SETTING') == "bar"

def test_existing(settings):
    set_from_environ(settings,
                     DJANGO__MEDIA_URL="bar")
    assert settings.get('MEDIA_URL') == "bar"

def test_json(settings):
    set_from_environ(settings,
                     DJANGO__json__NEW_SETTING='{"foo":"bar"}')
    assert settings.get('NEW_SETTING') == {"foo":"bar"}

def test_db(settings):
    set_from_environ(settings,
                     POSTGRES='postgres://uf07k1:wegauwhg@ec2-107-21-253-135.compute-1.amazonaws.com:5431/d8r82722',
                     DJANGO__db__DATABASES__default='$POSTGRES')
    assert settings['DATABASES']['default'] == {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8r82722',
        'HOST': 'ec2-107-21-253-135.compute-1.amazonaws.com',
        'USER': 'uf07k1',
        'PASSWORD': 'wegauwhg',
        'PORT': 5431,
    }

def test_list_edit(settings):
    set_from_environ(settings,
                     DJANGO__TEMPLATES__0__OPTIONS__context_processors__1='bar')
    assert settings["TEMPLATES"][0]["OPTIONS"]["context_processors"][1] == "bar"




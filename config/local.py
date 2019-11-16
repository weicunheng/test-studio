# -*- coding: utf-8 -*-
from config.default import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "test_studio",
        "PASSWORD": "test_studio",
        'USER': 'test_studio',
        "HOST": "127.0.0.1",
        "PORT": 5432,
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    }
}

# -*- coding: utf-8 -*-
from config.default import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "test_studio",
        "PASSWORD": "test_studio",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    }
}

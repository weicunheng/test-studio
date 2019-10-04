# -*- coding: utf-8 -*-

import os

if "ENVIRONMENT" in os.environ:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
else:
    ENVIRONMENT = {
        "local": "local",
        "development": "dev",
        "testing": "stag",
        "production": "prod",
    }.get("ENV", "local")

DJANGO_CONF_MODULE = "config.%s" % ENVIRONMENT

try:
    _module = __import__(DJANGO_CONF_MODULE, globals(), locals(), ['*'])
except ImportError as e:
    raise ImportError("Could not import config '%s' (Is it on sys.path?): %s"
                      % (DJANGO_CONF_MODULE, e))

for _setting in dir(_module):
    if _setting == _setting.upper():
        locals()[_setting] = getattr(_module, _setting)

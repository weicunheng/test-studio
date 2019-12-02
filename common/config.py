# -*- coding: utf-8 -*-
from django.conf import settings

if 'DEV' == settings.ENVIRON_NAME:
    # C端用户所属的特定组织机构ID
    CUSER_ORGANIZATION_ID = 51

elif 'PROD' == settings.ENVIRON_NAME:
    CUSER_ORGANIZATION_ID = 3

else:
    CUSER_ORGANIZATION_ID = 51

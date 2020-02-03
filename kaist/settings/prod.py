from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kaist',
        'USER': config_secret['aws']['aws_rds_user'],
        'PASSWORD': config_secret['aws']['aws_rds_password'],
        'HOST': config_secret['aws']['aws_rds_host'],
        'PORT': '3306',
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
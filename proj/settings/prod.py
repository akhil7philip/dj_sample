from .base import *  # noqa
from decouple import Csv, config
import os
import json 

ADMIN_NAME = os.getenv('ADMIN_NAME')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')

SUPPORT_EMAIL = os.getenv('SUPPORT_EMAIL', 'no-reply@apexive.com')

ADMINS = (
	(ADMIN_NAME, ADMIN_EMAIL),
)
MANAGERS = ADMINS

SECRET_KEY = os.environ.get("SECRET_KEY", 'testrouxhxiiaj6d-x=(-k^j%&5fcb1b)w8#$1yd91pn3#%%1i=u&uultvcv')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,.apexive.com', cast=Csv())

PROFILE = os.environ.get('DJANGO_CONFIGURATION', 'Dev')

if PROFILE == 'Prod':
	DEBUG = False
else:
	DEBUG = True
# CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_ALLOW_ALL = True

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_REGION = os.getenv('AWS_REGION')

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'ampq://rabbitmq:rabbitmq@rabbit')
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER_URL", "ampq://rabbitmq:rabbitmq@rabbit")

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')

PBI_EMAIL_USER 		= os.environ.get('PBI_EMAIL_USER')
PBI_EMAIL_PASSWORD 	= os.environ.get('PBI_EMAIL_PASSWORD')

DATABASES = {
	'default': {
		'ENGINE'	: 'django.db.backends.postgresql',
		'NAME'		: os.environ.get('DB_NAME', 'postgres'),
		'USER'		: os.environ.get('DB_USER', 'postgres'),
		'PASSWORD'	: os.environ.get('DB_PASSWORD', ''),
		'HOST'		: os.environ.get('DB_HOST', ''),
		'PORT'		: os.environ.get('DB_PORT', ''),
	},
	'sales': {
		'ENGINE'	: 'django.db.backends.postgresql',
		'NAME'		: os.environ.get('sales_NAME', 'postgres'),
		'USER'		: os.environ.get('sales_USER', 'postgres'),
		'PASSWORD'	: os.environ.get('sales_PASSWORD', ''),
		'HOST'		: os.environ.get('DB_HOST', ''),
		'PORT'		: os.environ.get('DB_PORT', ''),
	},
	'product': {
		'ENGINE'	: 'django.db.backends.postgresql',
		'NAME'		: os.environ.get('product_NAME', 'postgres'),
		'USER'		: os.environ.get('product_USER', 'postgres'),
		'PASSWORD'	: os.environ.get('product_PASSWORD', ''),
		'HOST'		: os.environ.get('DB_HOST', ''),
		'PORT'		: os.environ.get('DB_PORT', ''),
	},
}


GOOGLE_CLOUD_CREDENTIALS = json.loads(os.getenv('GOOGLE_CLOUD_CREDENTIALS'))

SAP_USER 		= os.getenv("SAP_USER")
SAP_PASSWORD	= os.getenv("SAP_PASSWORD")
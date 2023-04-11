from .base import *  # noqa
from decouple import Csv, config
import os
import json 

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
		'NAME'		: os.environ.get('SALES_NAME', 'postgres'),
		'USER'		: os.environ.get('SALES_USER', 'postgres'),
		'PASSWORD'	: os.environ.get('SALES_PASSWORD', ''),
		'HOST'		: os.environ.get('DB_HOST', ''),
		'PORT'		: os.environ.get('DB_PORT', ''),
	},
	'product': {
		'ENGINE'	: 'django.db.backends.postgresql',
		'NAME'		: os.environ.get('PRODUCT_NAME', 'postgres'),
		'USER'		: os.environ.get('PRODUCT_USER', 'postgres'),
		'PASSWORD'	: os.environ.get('PRODUCT_PASSWORD', ''),
		'HOST'		: os.environ.get('DB_HOST', ''),
		'PORT'		: os.environ.get('DB_PORT', ''),
	},
}

GOOGLE_CREDENTIALS = {
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
}
GOOGLE_AUTHORIZED_USER = {
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "client_secret": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    "refresh_token": "XXX"
}
GOOGLE_CLOUD_CREDENTIALS = {
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
}
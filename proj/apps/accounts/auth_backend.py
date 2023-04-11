import json
from datetime import timedelta
import uuid
import redis
import requests
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
import random

r = redis.Redis(host=settings.REDIS_HOST)

class AuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        redis_value = None
        '''
        get user details for session in cache;
        else fetch user details
        '''
        pass

def logout(request):
    pass


# Create your views here.
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.authtoken.models import Token


from .forms import (
    RegistrationForm,
    EditProfileForm
)


def register(request):
    pass


def view_profile(request, pk=None):
    pass


def edit_profile(request):
    pass
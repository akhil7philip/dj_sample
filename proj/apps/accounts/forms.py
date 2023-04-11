# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """
    A custom form for registration
    """
    pass


class EditProfileForm(UserChangeForm):
    """
    Custom form to edit profile
    """
    pass
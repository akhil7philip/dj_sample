# Create your models here.

import uuid

from crum import get_current_user
from django.contrib.auth.models import User,AnonymousUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token
from django.core.files import File
from django.conf import settings

User._meta.get_field('email')._unique = True


class NotificationType(models.TextChoices):
	GENERAL, SERVER_FAILURE = 'general', 'server_failure',

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=100, help_text="primary location", default='', blank=True)
	phone = PhoneNumberField(help_text="user's phone number", blank=True, null=True)
	image = models.ImageField(upload_to='profile_image', blank=True)
	is_enabled = models.BooleanField(default=True, help_text="Account Status")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(User, null=True, blank=True, related_name='profile_created',
								   on_delete=models.CASCADE)
	updated_by = models.ForeignKey(User, null=True, blank=True, related_name='profile_updated',
								   on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
	if created:
		user_profile_image_path = settings.RAW_ROOT + 'demo_profiles/blank.png'
		profile = UserProfile.objects.create(user=instance, is_enabled=True)
		with open(user_profile_image_path, 'rb') as f:
			file = File(f)
			profile.image.save(instance.username, file)
		profile.save()

@receiver(pre_save, sender=User)
def check_email(sender, instance, **kwargs):
	email = instance.email
	if sender.objects.filter(email=email).exclude(username=instance.username).exists():
		raise ValidationError('Email Already Exists')

# This receiver handles token and salt creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
		Salt.objects.create(user=instance)


@receiver(post_delete, sender=UserProfile)
def delete_profile_image(sender, instance=None, **kwargs):
	instance.image.delete(False)


@receiver(pre_save, sender=UserProfile, weak=False, )
def user_profile_callback(sender, instance=None, created=False, **kwargs):
	if instance._state.adding is True or instance.created_by is None:
		# we would need to create the object
		u = get_current_user()
		if u is not None and not isinstance(u, AnonymousUser):
			instance.created_by = get_current_user()
			instance.updated_by = get_current_user()
	else:
		# we are updating the object
		u = get_current_user()
		if u is not None and not isinstance(u, AnonymousUser):
			# we are updating the object
			instance.updated_by = get_current_user()


class Salt(models.Model):
	""" This class represents the unique User Salt model """
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Salt'
		verbose_name_plural = 'Salts'

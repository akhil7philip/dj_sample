from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ExportActionModelAdmin
from import_export.formats import base_formats
from rangefilter.filters import DateTimeRangeFilter

# Register your models here.
from .models import UserProfile, UserNotificationSettings


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'image_view', 'location', 'phone', 'created_at', 'updated_at')
	list_filter = ('location', ('updated_at', DateTimeRangeFilter), 'updated_by')
	readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')

	def user_name(self, obj):
		return obj.user

	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('location', 'user')

		return queryset

	def image_view(self, obj):
		image_url = ''
		try:
			image_url = format_html('<img src="{url}" height={height} />'.format(
				url=obj.image.url,
				height=100
			))
		except:
			pass
		return image_url

	user_name.short_description = 'Username'


class UserNotificationSettingsAdmin(ExportActionModelAdmin):
	pass




# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserNotificationSettings, UserNotificationSettingsAdmin)

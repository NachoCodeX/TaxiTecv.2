from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

# admin.site.register(Admin)
admin.site.register(Owner)
admin.site.register(Driver)

admin.site.unregister(User)
class UserProfileInline(admin.StackedInline):
	model=UserProfile

class UserProfileAdmin(UserAdmin):
	inlines=[
		UserProfileInline,
	]

admin.site.register(User,UserProfileAdmin)

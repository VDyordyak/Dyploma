from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Subject , Quiz, Not_Singup_User

# Register your models here.
admin.site.site_header ="University Student Testing Platform"
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Not_Singup_User)
admin.site.unregister(Group)
# Register out own model admin, based on the default UserAdmin

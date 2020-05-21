from django.contrib import admin

 # Register your models here.
from .models import Events 
from django.contrib.auth.admin import UserAdmin
from .models import MyUser



admin.site.register(Events)






admin.site.register(MyUser, UserAdmin)
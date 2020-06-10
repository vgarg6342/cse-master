from django.contrib import admin
from .models import Contact,Question, UserQuizData

# Register your models here.
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(UserQuizData)


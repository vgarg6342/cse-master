from django.db import models

# Create your models here.
class Contact(models.Model):
	User      = models.TextField(default="user name")
	Comment   = models.TextField(default="user name")


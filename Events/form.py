from django import forms
from .models import MyUser

class Userform(forms.ModelForm):
	class Meta:
		model = MyUser
		fields =['age', 'college']

class forma(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)

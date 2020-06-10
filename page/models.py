from django.db import models
from photologue.models import Gallery
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Contact(models.Model):
	User      = models.TextField(default="user name")
	Comment   = models.TextField(default="user name")

# every correct answer will increment the counter and in turn it will fetch the question
# hence counter need to be from 1 to 10 with increaseing order of the level
# we will take quiz name and current counter as an input and fetch the question
# hence no need to have a client side rendering
class Question(models.Model):
	typeans = (
	('WEB', 'webbed'),
	('MAT', 'mathematrix'), 
	('CUB', 'cubbed'), 
	('AST', 'astronomy'),   
)
	quiz_name        = models.CharField(max_length=3, choices=typeans)
	unique_id        = models.TextField(default= "eg- wb1", unique = True)
	question_no      = models.IntegerField(default = 1) 
	question         = models.TextField(default= "question")
	answer           = models.TextField(default= "answer")
	queation_img_url = models.TextField(null = True)
	question_image   = models.ForeignKey(
		Gallery,
		on_delete=models.CASCADE,
		blank=True, 
		related_name='questionimage',
		null = True
		)
	def __str__(self):
			return '{}'.format(self.unique_id)

	def save(self,*args,**kwargs):
		self.queation_img_url = ""
		if self.question_image is not None:
			for photo in self.question_image.photos.all():
				full_urls = ''.join(['http://', 'localhost:8000', photo.get_display_url()])
				self.queation_img_url += full_urls + " "
		super(Question, self).save(*args, **kwargs)

class UserQuizData(models.Model):

	typeans = (
	('WEB', 'webbed'),
	('MAT', 'mathematrix'), 
	('CUB', 'cubbed'), 
	('AST', 'astronomy'),   
)
	quiz_name    = models.CharField(max_length=3, choices=typeans)
	counter      = models.IntegerField(default = 1)
	user         = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		blank=True, 
		related_name='user',
		null = True
		)


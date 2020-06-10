from django.db import models
from photologue.models import Gallery
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.shortcuts import get_current_site




# Create your models here.
class Events(models.Model):
	serial_no           = models.IntegerField(null = 'True')
	event_id            = models.TextField(default = "must be same with the usermodel TextField")
	event_name          = models.TextField(default = 'Event', max_length = 50)
	event_speaker       = models.TextField(default = 'vivek',max_length = 50)
	event_date          = models.DateField(null = 'True')
	event_place         = models.TextField(default = 'Event')
	discription         = models.TextField(default = 'short note')
	event_rules         = models.TextField(default = 'all rules must go there')
	event_summary       = models.TextField(default = 'complete summary')
	gallery_url         = models.TextField(blank=True, default = "Y", null = True)
	coordinator_url     = models.TextField(blank=True, default = "Y", null = True)
	typeans = (
	('ONL', 'online'),
	('OFF', 'offline'),
	('WOR', 'workshops'),
	('MAJ', 'majorEvents'), 
	('QUZ', 'quiz'), 
)
	event_type          = models.CharField(max_length = 3, choices = typeans, null = True )
	event_gallery       = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        blank=True, 
        related_name='gallery',
        null = True
        
    )
	event_coordinator  = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        blank=True, 
        related_name='coord_gallery',
        null = True
    )
	
	def __str__(self):
			return '{}'.format(self.event_name)

	def save(self, *args, **kwargs):
		self.gallery_url = ""
		for photo in self.event_gallery.photos.all():
			full_url = ''.join(['http://', 'localhost:8000', photo.get_display_url()])
			self.gallery_url += full_url + " "

		self.coordinator_url = ""
		if self.event_coordinator is not None:
			for photo in self.event_coordinator.photos.all():
				full_urls = ''.join(['http://', 'localhost:8000', photo.get_display_url()])
				self.coordinator_url += full_urls + " "
		super(Events, self).save(*args, **kwargs)

class MyUser(AbstractUser):
	typeans = (
	('Y', 'YES'),
	('N', 'NO'),   
)
	battleofbands = models.CharField(max_length=1, choices=typeans, default= 'N')
	groupdance    = models.CharField(max_length=1, choices=typeans, default= 'N')
	# add all the events and workshops as in the above example
	college       = models.TextField(default = 'IIST')
	mobile_no     = models.IntegerField(default = '1234567890')
	gender        = models.TextField(default = 'dont be sexist')
	age           = models.IntegerField(default = '18')






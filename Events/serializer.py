from .models import MyUser, Events
from photologue.models import Gallery, Photo
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
	# all the input to the usermodel will use this serializer which will display on dashboard
    class Meta:
        model = User
        fields = ['battleofbands', 'groupdance', 'age', 'college', 'username']

class UserRegistrationEventSerializer(serializers.HyperlinkedModelSerializer):
	# all the events must go here
    class Meta:
        model = User
        fields = ['battleofbands', 'groupdance']

class EventSerializer(serializers.HyperlinkedModelSerializer):
     # general purpose ie all the display of events will happen here
	class Meta:
		model  = Events
		fields = ['gallery_url','event_name', 'discription', 'serial_no','event_type', 'event_id']

class EventDataSerializer(serializers.HyperlinkedModelSerializer):
    # for specific events details
	class Meta:
		model  = Events
		fields = ['event_speaker', 'gallery_url','event_name', 'discription', 'serial_no', 'event_rules', 'event_date','event_id']

class UserAddSerializer(serializers.HyperlinkedModelSerializer):
	# additional detals for user input
    class Meta:
        model = User
        fields =['age', 'college', 'mobile_no', 'gender']




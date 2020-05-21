from .models import MyUser, Events
from photologue.models import Gallery, Photo
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['battleofbands', 'groupdance', 'age', 'college', 'username']

class UserRegistrationEventSerializer(serializers.HyperlinkedModelSerializer):
	# all the events must go here
    class Meta:
        model = User
        fields = ['battleofbands', 'groupdance']

class EventSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model  = Events
		fields = ['gallery_url','event_name', 'discription', 'serial_no']

class EventDataSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model  = Events
		fields = ['event_speaker', 'gallery_url','event_name', 'discription', 'serial_no', 'event_rules', 'event_date']

class UserAddSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =['age', 'college', 'mobile_no', 'gender']




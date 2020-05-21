
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['User','Comment']

class TokenSerializer(serializers.Serializer):
    idtoken = serializers.CharField(max_length=None, min_length=None)
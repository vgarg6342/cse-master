
from rest_framework import serializers
from .models import Contact, Question, UserQuizData

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['User','Comment']

class TokenSerializer(serializers.Serializer):
    idtoken = serializers.CharField(max_length=None, min_length=None)

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model   = Question
		fields  = ['quiz_name', 'question', 'question_no', 'unique_id']

class UserQuizDataSerializer(serializers.Serializer):
	class Meta:
		model  = UserQuizData
		fields = ['quiz_name', 'counter']
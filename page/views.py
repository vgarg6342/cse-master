from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Contact, Question, UserQuizData
from .serializers import ContactSerializer, TokenSerializer, QuestionSerializer, UserQuizDataSerializer
from django.contrib.auth import logout
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
User = get_user_model()

from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.authtoken.models import Token


class RegisterAPI(APIView):

    def post(self,request):
        serializer = TokenSerializer(data = request.data)
        if serializer.is_valid():
            tokendata = serializer.validated_data["idtoken"] 
            tokendata = request.data['idtoken']        
            try:
                idinfo = id_token.verify_oauth2_token(tokendata, requests.Request(), '66922569807-nn0ubkp1qjm4q89n5schp67mgg4jap8u.apps.googleusercontent.com')          
                if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                    return Response({"error": "user don't exist"})
                # ID token is valid. Get the user's Google Account ID from the decoded token.
                if User.objects.filter(email = idinfo['email']).first() is None:
                    password = User.objects.make_random_password()
                    user = User.objects.create_user(username=idinfo['email'], first_name= idinfo['name'], email =idinfo['email'], password = 'password')
                    
                else: 
                    user = User.objects.get(username = idinfo['email'])
                tokenid, created = Token.objects.get_or_create(user = user)
                return Response(data= {"name":idinfo['name'], "email": idinfo['email'], "token": tokenid.key })     
                                             
            except ValueError:
                # Invalid token
                return Response({"error": "invalid token"})
        else: Response({"error": "invalid data input"})

# end points for handling the quiz starts from here.

@api_view(('GET',))
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_question(request):
    quiz     = request.headers['quiz-name']
    counter  = request.headers['question-no']
    # take question number from the counter storing userdata and quiz name from the headers
    data = UserQuizData.objects.filter(quiz_name__contains = request.headers['quiz-name']).filter(user = request.user)[0]
    question = Question.objects.filter(quiz_name__contains = quiz).filter(question_no = data.counter)[0]  
    serializer = QuestionSerializer(question)
    return Response(serializer.data)

@api_view(('POST',))
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_quiz_registration(request):
    User = request.user
    quiz = request.headers['quiz-name']
    data = UserQuizData(quiz_name = quiz, user = User, counter = 1)
    data.save()
    return Response({'alert': 'sucessfull'})

@api_view(('POST',))
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def quiz_answer_check(request):
    answer      = request.headers['answer']
    unique_id   = request.headers['unique-id']
    correct_ans = Question.objects.get(unique_id = unique_id).answer
    if answer == correct_ans:
        data = UserQuizData.objects.filter(quiz_name__contains = request.headers['quiz-name']).filter(user = request.user)[0]
        data.counter += 1
        data.save()
        return Response({'alert': 'correct answer'})
    return Response({'alert': 'wrong answer'})

# TODO untested method need some refinements
@api_view(('GET',))
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def leaderboard(request):
    quiz = request.headers['quiz-name']
    data = UserQuizData.objects.filter(quiz_name__contains =quiz ).filter(
    counter__gte=UserQuizData.objects.order_by('-counter')[9].counter
    )[:10]
    serializer = UserQuizDataSerializer(data, many =True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def contact_list(request):

    if request.method == 'GET':
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        print(serializer)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.User)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer, TokenSerializer
from django.contrib.auth import logout
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()

from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.authtoken.models import Token

# (Receive token by HTTPS POST)
# ...

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




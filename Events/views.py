from django.shortcuts import render
from .models import Events,MyUser
from photologue.models import Gallery
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializer import UserSerializer, EventSerializer, UserAddSerializer, EventDataSerializer, UserRegistrationEventSerializer
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .models import  MyUser
from .models import Events as Event
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def about_us(request):

	return render(request,"home.html",{})

class Events(APIView):
    def get(self, request, format=None):
        queryset = Event.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = EventSerializer(queryset, context=serializer_context, many=True)
        return Response(serializer.data)

class EventDiscription(APIView):

    def get_object(self, event_id):
        try:
            return Event.objects.get(event_id = event_id)
        except Events.DoesNotExist:
            raise Http404

    def get(self, request,event_id, format=None):
        event = self.get_object(event_id)
        serializer = EventDataSerializer(event)
        return Response(serializer.data)

# remove this function in production
class UserViewSet(viewsets.ModelViewSet):
	queryset           = MyUser.objects.all()
	serializer_class   = UserSerializer
	permission_classes = [permissions.AllowAny]

#set redirect url in google authentication for the users to fill data
class UserDetail(APIView):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication, ) 
    def get_object(self, username):
        
        try:
            return User.objects.get(username = username)
        except MyUser.DoesNotExist:
            raise Http404
         
    def put(self, request, format=None):
        User       = self.get_object(request.user)
        serializer = UserAddSerializer(User, data=request.headers)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

# user will register for event by this method
class UserRegistrationEvent(APIView):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication, ) 
    def get_object(self, username):
        try:
            return User.objects.get(username = username)
        except MyUser.DoesNotExist:
            raise Http404
         
    def put(self, request, format=None):
        
        User       = self.get_object(request.user)
        serializer = UserRegistrationEventSerializer(User, data=request.headers)
        if serializer.is_valid():
            serializer.save()
            return Response({'alert': 'registration successful'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#changes in serializaers to show to the user
@api_view(('GET',))
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def UserISAuthenticated(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

# for admin purposes
def AdminEvents(request):
    if request.user.is_superuser:
        qs       = Event.objects.all()
        context  = {
            'object_list': qs,
        }
        return render(request,"eventlog.html", context)
# for admin purposes
def AdminEventUsers(request,id):
    if request.user.is_superuser:
        qs = MyUser.objects.filter(id__icontains = "Y")
        context ={
            'object_list': qs
        }
        return render(request,"event-user.html", context)

    



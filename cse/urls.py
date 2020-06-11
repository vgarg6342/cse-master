from django.conf.urls import url
from django.urls import path, include
from photologue.sitemaps import GallerySitemap, PhotoSitemap
from django.conf import settings
from django.conf.urls.static import static
"""cse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Events.views import about_us, EventDiscription, UserViewSet, Events, UserDetail, UserISAuthenticated, AdminEvents, AdminEventUsers,UserRegistrationEvent
from django.conf import settings
from rest_framework import routers
from page.views import  RegisterAPI, get_question, user_quiz_registration, quiz_answer_check,leaderboard
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('users',UserViewSet, basename='MyUser')




urlpatterns = [

    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    path('admin/', admin.site.urls),
    path('',about_us,name= "about"),
    path('events/',Events.as_view(),name= "events"),
    path('events/<str:event_id>/',EventDiscription.as_view(),name= "discription"),
    path('user-registration/' , UserRegistrationEvent.as_view()),
    path('', include('page.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('add/', UserDetail.as_view(), name = "useradd"),
    path('', include(router.urls)),
    path('isauthenticated/', UserISAuthenticated, name= "authenticated"),
    path('adminevents/', AdminEvents, name = "adminevents"),
    path('adminevents/<str:id>', AdminEventUsers),
    path('register/',RegisterAPI.as_view()),
    path('question/',get_question),
    path('quiz-reg/', user_quiz_registration),
    path('answer-check/',quiz_answer_check),
    path('leaderboard/',leaderboard)

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




sitemaps = {
            'photologue_galleries': GallerySitemap,
            'photologue_photos': PhotoSitemap,
            
            }

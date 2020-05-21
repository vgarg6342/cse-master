from django.urls import path
from page import views

urlpatterns = [
    path('contact/', views.contact_list),
    
]
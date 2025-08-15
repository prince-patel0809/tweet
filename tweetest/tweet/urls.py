from . import views
from django.urls import path

urlpatterns = [
     path('', views.tweet_list, name='tweet_list'),
     path('create/', views.tweet_create, name='tweet_create'),
     path('<int:tweet_id>/edit/', views.tweet_edite, name='tweet_edite'),
     path('<int:tweet_id>/', views.tweet_delete, name='tweet_delete'),
     path('register/', views.register, name='register'),
   
     

] 

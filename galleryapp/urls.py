from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('home', views.home, name='home'),
    path('posts', views.posts, name='posts'),
    path('logout', views.exit, name='exit'),
    path('register', views.register, name='register')   
]

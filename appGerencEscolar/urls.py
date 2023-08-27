from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.signUp, name='signUp'),
    path('home/', views.home, name='home'),
    
]

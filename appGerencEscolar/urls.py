from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('cadastro/', views.signUp, name='signUp'),
    path('home/', views.home, name='home'),
<<<<<<< HEAD
    # path('turmas/', views.turmas, name='turmas'),
    # path('cadastro/', views.cadastro, name='cadastro'),
    # path('subscribe/', views.alunos, name='cadastroaluno')
=======
>>>>>>> parent of 43fb61b (database created)
    
]

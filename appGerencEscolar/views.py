from django.shortcuts import render
from .models import Aluno
from .models import Professor
from .models import Turma
import pandas as pd
import smtplib
import email.message
import random

def login(request):
    return render(request, 'login.html')


def signUp(request):
    return render(request, 'signUp.html')

def home(request):
<<<<<<< HEAD
    return render(request, 'home.html')

def turmas(request):
    return render(request, 'turmas.html')

# def cadastro(request):
#     return render(request, 'cadastroaluno.html')

# GERADOR DE RA

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ra = ""


for i in range(1, 3):
  ra += random.choice(letters)

for i in range(1, 5):
  ra += random.choice(numbers)

# print(ra.upper())


# ADICIONAR ALUNO

def alunos(request):
   if request.method == 'Post':
      pass
    # novo_aluno = Aluno()
    # novo_aluno.nomeAluno = request.POST.get('nome_aluno')
    # novo_aluno.raAluno = ra
    # novo_aluno.telAluno = request.POST.get('telefone_aluno')
    # # novo_aluno.nascAluno = request.POST.get('nasc_Aluno')
    # novo_aluno.emailAluno = request.POST.get('email_aluno')
    # # novo_aluno.turmaAluno = request.POST.get('turma_aluno')
    # novo_aluno.save()
    

    # alunos = {
    #     'alunos': Aluno.objects.all()
    # }

    # # Definir o render
    # print("novo_aluno")
    # return render(request, 'templates/lin.html', alunos)
=======
    return render(request, 'home.html')
>>>>>>> parent of 43fb61b (database created)

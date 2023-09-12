from django.db import models

class Aluno(models.Model):
    idAluno = models.CharField(primary_key=True, max_length=4)
    raAluno = models.CharField(max_length=6)
    nomeAluno = models.CharField(max_length=100)
    emailAluno = models.CharField(max_length=100, default='DEFAULT VALUE')
    # nascAluno = models.DateField(default='0000-00-00')
    telAluno = models.IntegerField()
    
class Professor(models.Model):
    idProfessor = models.CharField(primary_key=True, max_length=4)
    nomeProfessor = models.CharField(max_length=100)
    emailProfessor = models.CharField(max_length=100)
    materiaProfessor = models.CharField(max_length=50)

class Turma(models.Model):
    idTurma = models.CharField(primary_key=True, max_length=4)
    nomeTurma = models.CharField(max_length=50)
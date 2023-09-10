# Generated by Django 4.2.4 on 2023-09-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGerencEscolar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('idProfessor', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nomeProfessor', models.CharField(max_length=100)),
                ('emailProfessor', models.CharField(max_length=100)),
                ('materiaProfessor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('idTurma', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nomeTurma', models.CharField(max_length=50)),
            ],
        ),
    ]
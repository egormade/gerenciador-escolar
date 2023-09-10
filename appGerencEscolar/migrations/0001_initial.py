# Generated by Django 4.2.4 on 2023-09-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('idAluno', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('raAluno', models.CharField(max_length=6)),
                ('nomeAluno', models.CharField(max_length=100)),
                ('emailAluno', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('nascAluno', models.DateField(default='0000-00-00')),
                ('telAluno', models.IntegerField()),
            ],
        ),
    ]
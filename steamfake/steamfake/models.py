from django.db import models

# Create your models here.

# EXECUTAR NO WORKBENCH PARA CRIAR O DATA BASE 
# CREATE DATABASE steam_fake_db CHARACTER SET UTF8MB4;
# py manage.py makemigrations
# py manage.py migrate 


class Categoria(models.Model):
    nome = models.CharField(max_length=23, unique=True)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=23, unique=True)
    desc = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nome, self.desc
    

# class Aluno(models.Model):
#     nome = models.CharField(max_length=10) # VARCHAR
#     # idade = models.IntegerField(default=0) # INT -- removido 
#     nota1 = models.DecimalField(default=0, decimal_places=2, max_digits=4)
#     nota2 = models.DecimalField(default=0, decimal_places=2, max_digits=4)
#     nota3 = models.DecimalField(default=0, decimal_places=2, max_digits=4)


# class Curso(models.Model):
#     nome = models.CharField(max_length=15)
#     duracao = models.IntegerField(default=0)


# class Turma(models.Model):
#     data_inicio = models.DateTimeField()
#     curso = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=True,
#     null=True)
    
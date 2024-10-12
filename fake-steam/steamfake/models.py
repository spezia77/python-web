from django.db import models

# Create your models here.

# EXECUTAR NO WORKBENCH PARA CRIAR O DATA BASE 
# CREATE DATABASE steam_fake_db CHARACTER SET UTF8MB4;

class Categoria(models.Model):
    nome = models.CharField(max_length=23, unique=True)
    

# Generated by Django 5.1.2 on 2024-10-14 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steamfake', '0004_aluno_nota1_aluno_nota2_aluno_nota3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='idade',
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamfake', '0002_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='idade',
            field=models.IntegerField(default=0),
        ),
    ]

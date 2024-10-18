# Generated by Django 5.1.2 on 2024-10-18 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamfake', '0011_tag_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('data_lancamento', models.DateField()),
                ('foto_capa', models.ImageField(null=True, upload_to='jogos_capa')),
                ('desenvolvedora', models.CharField(max_length=100, null=True)),
                ('descricao', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='steamfake.categoria')),
            ],
        ),
    ]

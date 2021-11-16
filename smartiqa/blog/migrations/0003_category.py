# Generated by Django 3.2.6 on 2021-11-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kategoriya nomi')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
            ],
        ),
    ]

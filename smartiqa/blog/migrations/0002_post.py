# Generated by Django 3.2.6 on 2021-11-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Maqola nomi')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='*')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='post_Images/', verbose_name='Maqola rasmi')),
                ('description', models.TextField(verbose_name='Maqoala matni')),
                ('author', models.CharField(default='Admin', max_length=50)),
            ],
        ),
    ]

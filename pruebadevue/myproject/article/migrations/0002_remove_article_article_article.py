# Generated by Django 2.0.7 on 2018-07-15 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_article',
        ),
    ]

# Generated by Django 2.2.3 on 2019-08-06 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
    ]

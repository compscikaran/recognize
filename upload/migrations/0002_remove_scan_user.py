# Generated by Django 2.0.3 on 2018-03-26 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scan',
            name='user',
        ),
    ]
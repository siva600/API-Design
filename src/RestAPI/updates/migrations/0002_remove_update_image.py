# Generated by Django 2.2 on 2019-04-12 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='image',
        ),
    ]

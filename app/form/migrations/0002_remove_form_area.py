# Generated by Django 2.2.4 on 2019-09-04 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='area',
        ),
    ]

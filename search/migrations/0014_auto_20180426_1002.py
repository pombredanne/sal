# Generated by Django 1.10 on 2018-04-26 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0013_searchcache'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchrow',
            name='search_models',
            field=models.CharField(choices=[('Machine', 'Machine'), ('Facter', 'Facter'), ('Condition', 'Condition'), ('External Script', 'External Script'), ('Application Inventory', 'Application Inventory'), ('Application Version', 'Application Version'), ('Profile', 'Profile'), ('Profile Payload', 'Profile Payload')], default='AND', max_length=254, verbose_name='Search item'),
        ),
    ]

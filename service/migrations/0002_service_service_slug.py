# Generated by Django 4.1.3 on 2022-12-01 09:03

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='service_title', unique=True),
        ),
    ]

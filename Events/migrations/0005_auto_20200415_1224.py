# Generated by Django 2.2.2 on 2020-04-15 06:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_auto_20200406_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='coordinator_url',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, default='Y', null=True), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='events',
            name='gallery_url',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, default='Y', null=True), size=None), size=None),
        ),
    ]

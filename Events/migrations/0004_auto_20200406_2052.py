# Generated by Django 2.2.2 on 2020-04-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_auto_20200406_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='coordinator_url',
            field=models.TextField(default='y ', null='True'),
        ),
        migrations.AlterField(
            model_name='events',
            name='gallery_url',
            field=models.TextField(default='Y', null='True'),
        ),
    ]

# Generated by Django 2.2.2 on 2020-04-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0009_auto_20200415_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='gallery_url',
            field=models.TextField(blank=True, default='Y', null=True),
        ),
    ]

# Generated by Django 2.2.2 on 2020-04-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_auto_20200415_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mobile_no',
            field=models.IntegerField(default='1234567890'),
        ),
    ]

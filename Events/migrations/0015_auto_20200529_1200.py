# Generated by Django 2.2.2 on 2020-05-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0014_auto_20200529_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_name',
            field=models.TextField(default='Event', max_length=50),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_speaker',
            field=models.TextField(default='vivek', max_length=50),
        ),
    ]
# Generated by Django 2.0.7 on 2019-09-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.TextField(default='user name')),
                ('Comment', models.TextField(default='user name')),
            ],
        ),
    ]

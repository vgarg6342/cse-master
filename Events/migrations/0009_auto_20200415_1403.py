# Generated by Django 2.2.2 on 2020-04-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0008_auto_20200415_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='gallery_url',
            field=models.SlugField(max_length=300, null=True),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_auto_20210129_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
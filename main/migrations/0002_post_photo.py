# Generated by Django 3.1.4 on 2020-12-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.FileField(default=0, upload_to='main/uploads/'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-31 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210331_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dis_like',
            field=models.IntegerField(default=0),
        ),
    ]

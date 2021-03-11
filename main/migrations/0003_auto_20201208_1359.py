# Generated by Django 3.1.4 on 2020-12-08 08:59

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_h',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='img_w',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=0, height_field='img_h', upload_to=main.models.convert_fn, width_field='img_w'),
        ),
    ]

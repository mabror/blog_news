# Generated by Django 3.1.7 on 2021-03-31 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_dis_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dis_like',
            new_name='dislike',
        ),
    ]

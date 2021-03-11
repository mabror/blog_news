from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
import os
from io import BytesIO
from django.core.files import File
from django.utils.translation import get_language


def convert_fn(self, file):
    ext = file.split('.')[-1]
    file = '{:Y%-%m-%d-%H-%M-%S}.{}'.format(datetime.now(), ext)
    return os.path.join('main/uploads', file)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    title_uz = models.CharField(max_length=100, null=True, blank=True)
    title_ru = models.CharField(max_length=100, default=None, null=True, blank=True)
    title_en = models.CharField(max_length=100, default=None, null=True, blank=True)
    content_uz = models.TextField(null=True, blank=True)
    content_ru = models.TextField(default=None, null=True, blank=True)
    content_en = models.TextField(default=None, null=True, blank=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    post_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default="download.jpeg",
                              upload_to=convert_fn,
                              blank=True,
                              null=True,
                              width_field='img_w',
                              height_field='img_h',
                              )

    img_w = models.IntegerField(default=0)
    img_h = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # print(self.photo.closed)
        if not self.photo.closed:
            img = Image.open(self.photo)
            img.thumbnail((500, 500), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')
            print(self.photo)
            # tmp.seek(0)

            self.photo = File(tmp, 'image.png')
        return super().save(*args, **kwargs)

    @property
    def title(self):
        column = 'title_{}'.format(get_language())
        return getattr(self, column)

    @property
    def content(self):
        column = 'content_{}'.format(get_language())
        return getattr(self, column)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

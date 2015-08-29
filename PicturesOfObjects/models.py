# coding=utf-8
from PollutionMark.models import PollutionMark
from django.contrib.auth.models import User
from django.db import models


class PicturesOfObjects(models.Model):
    pollution_mark = models.ForeignKey(PollutionMark, related_name='pictures')
    full_photoURL = models.FileField(verbose_name='Изображение', upload_to='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PicturesOfObjects'
        verbose_name_plural = 'PicturesOfObjects'

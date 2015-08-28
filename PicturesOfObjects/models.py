# coding=utf-8
from PollutionMark.models import PollutionMark
from django.contrib.auth.models import User
from django.db import models


class PicturesOfObjects(models.Model):
    pollution_mark = models.ForeignKey(PollutionMark)
    full_photoURL = models.FileField(verbose_name='Изображение', upload_to='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'PicturesOfObjects'
        verbose_name_plural = 'PicturesOfObjects'


    def save(self, *args, **kwargs):
        """ Собственный метод для заполнения поля с первичным ключём."""
        # if not self.uid or self.uid == u'':
        #     self.uid = uuid.uuid4().get_hex()

        # slug_str = "%s %s" % (self.name_en, self.part_speech)
        # slug_str = "%s" % (self.uid)
        # self.slug = self.make_slug(self.name_en)

        super(PicturesOfObjects, self).save(*args, **kwargs)
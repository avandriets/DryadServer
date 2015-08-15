# coding=utf-8
from django.contrib.auth.models import User
from django.db import models


class PollutionMark(models.Model):
    headline = models.CharField(verbose_name='Заголовок', max_length=100, help_text='Заголовок сообщения')
    full_description = models.CharField(verbose_name='Описание', max_length=600, null=True, blank=True, help_text='Подробное описание проблемы')
    full_photoURL = models.FileField(verbose_name='Изображение', upload_to='media/images', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True, blank=True, help_text='Долгота')
    latitude = models.FloatField(verbose_name='Широта', null=True, blank=True, help_text='Широта')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)

    class Meta:
        db_table = 'PollutionMark'
        verbose_name_plural = 'PollutionMark'

    def __unicode__(self):
        return u'%s' % (self.headline)

    def save(self, *args, **kwargs):
        """ Собственный метод для заполнения поля с первичным ключём."""
        # if not self.uid or self.uid == u'':
        #     self.uid = uuid.uuid4().get_hex()

        # slug_str = "%s %s" % (self.name_en, self.part_speech)
        # slug_str = "%s" % (self.uid)
        # self.slug = self.make_slug(self.name_en)

        super(PollutionMark, self).save(*args, **kwargs)

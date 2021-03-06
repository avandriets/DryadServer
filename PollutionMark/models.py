# coding=utf-8
import VoteUsers
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

TYPE_OF_RECORD = ((1, 'Фотофакт'), (2, 'Инициатива'), (3, 'Гражданский проект'))


class PollutionMark(models.Model):
    headline = models.CharField(verbose_name='Заголовок', max_length=100, help_text='Заголовок сообщения')
    full_description = models.CharField(verbose_name='Описание', max_length=600, null=True, blank=True, help_text='Подробное описание проблемы')
    longitude = models.FloatField(verbose_name='Долгота', null=True, blank=True, help_text='Долгота')
    latitude = models.FloatField(verbose_name='Широта', null=True, blank=True, help_text='Широта')
    attitude = models.FloatField(verbose_name='Высота', null=True, blank=True, help_text='Высота')
    type = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)

    @property
    def vote_yes(self):
        count = VoteUsers.models.Vote.objects.filter(pollution_mark=self).aggregate(Sum('vote_yes'))
        if count['vote_yes__sum'] is None:
            return 0
        return count['vote_yes__sum']

    @property
    def vote_no(self):
        count = VoteUsers.models.Vote.objects.filter(pollution_mark=self).aggregate(Sum('vote_no'))
        if count['vote_no__sum'] is None:
            return 0
        return count['vote_no__sum']

    class Meta:
        db_table = 'PollutionMark'
        verbose_name_plural = 'PollutionMark'
        ordering = ['updated_at']

    def __unicode__(self):
        return u'%s' % (self.headline)

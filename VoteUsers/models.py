# coding=utf-8
from PollutionMark.models import PollutionMark
from django.contrib.auth.models import User
from django.db import models


class Vote(models.Model):
    pollution_mark = models.ForeignKey(PollutionMark, related_name='vote')
    comment = models.CharField(verbose_name='Конмментарий', max_length=600, null=True, blank=True, help_text='Конмментарий')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True)

    class Meta:
        db_table = 'Vote'
        verbose_name_plural = 'Votes'

    def save(self, *args, **kwargs):
        super(Vote, self).save(*args, **kwargs)

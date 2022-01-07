from django.db import models

from this_you_not_hello_word.models import TrackableUpdateCreateModel


class NewsPost(TrackableUpdateCreateModel):
    title = models.CharField(max_length=256, null=True, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание новостного поста')

    class Meta:
        verbose_name = 'Новостной пост'
        verbose_name_plural = 'Новостные посты'

    def __str__(self):
        return self.title

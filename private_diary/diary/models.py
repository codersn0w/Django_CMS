from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Diary(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete = models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    class Meta:
        verbose_name_plural = 'Diary'
    def __str__(self):
        return self.title
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

import django.utils.timezone



class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')



class Archivement(models.Model):
    archive_name = models.CharField(max_length=80)
    archive_info = models.TextField(max_length=800)
    archive_tier = models.IntegerField(default=0)
    def __str__(self):
        return self.archive_name



class Clear_archivement(models.Model):
    user_id = models.ForeignKey('User', related_name='user_archive', on_delete=models.CASCADE, db_column='user_id')
    archive_id = models.ForeignKey('Archivement', related_name='archivement', on_delete=models.CASCADE, db_column='archive_id')
    archive_date = models.DateTimeField(default=django.utils.timezone.now)
    def __str__(self):
        return self.user_id + ' ' + self.archive_id



class Board(models.Model):
    board_name = models.CharField(max_length=80)
    board_type = models.IntegerField(default=0)
    def __str__(self):
        return self.board_name



class Bulletin(models.Model):
    user_id = models.ForeignKey('User', related_name='user_bulletin', on_delete=models.CASCADE, db_column='user_id')
    board_id = models.ForeignKey('Board', related_name='board', on_delete=models.CASCADE, db_column='board_id')
    bulletin_title = models.CharField(max_length=80)
    bulletin_contents = models.TextField(max_length=8000)
    bulletin_write_date = models.DateTimeField(default=django.utils.timezone.now)
    bulletin_last_edit_date = models.DateTimeField(auto_now=True)
    bulletin_recommend = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_notice = models.BooleanField(default=False)
    tag_id = models.ManyToManyField('Recycle_tag', blank=True, related_name='recycle')
    def __str__(self):
        return self.bulletin_title


class Recycle_tag(models.Model):
    tag_name_korean = models.CharField(max_length=80)
    tag_name_english = models.CharField(max_length=20)
    tag_info = models.TextField(max_length=800)
    def __str__(self):
        return self.tag_name_korean



class Memo(models.Model):
    bulletin = models.ForeignKey('Bulletin', related_name='bulletin_meno', on_delete=models.CASCADE)
    memo_contents = models.CharField(max_length=4000)
    user_id = models.ForeignKey('User', related_name='user', on_delete=models.CASCADE, db_column='user_id')
    memo_write_date = models.DateTimeField(default=django.utils.timezone.now)
    memo_recommend = models.BigIntegerField(default=0)
    memo_color = models.CharField(max_length=6)
    def __str__(self):
        return self.memo_contents

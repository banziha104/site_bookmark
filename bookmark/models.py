from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bookmark(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True, null=True) # Char 필드 생성
    url = models.URLField('url',unique=True)

    def __str__(self): # 어떤값을 보여줄지
        return self.title


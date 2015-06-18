from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  url = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  author = models.ForeignKey(User)
  body = models.TextField()

  def __unicode__(self):
    return self.title

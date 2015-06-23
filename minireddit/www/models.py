from django.db import models
from django.contrib.auth.models import User

class Sub(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='created_subs')
    subscribers = models.ManyToManyField(User, related_name='subscribed_to')

    def __unicode__(self):
        return self.name

class Post(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User)
    body = models.TextField()
    sub = models.ForeignKey(Sub)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField()
    parent_id = models.ForeignKey(Comment)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.author.username


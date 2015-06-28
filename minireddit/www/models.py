from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
import json

class Sub(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='created_subs')
    subscribers = models.ManyToManyField(User, related_name='subscribed_to')

    def dump(self):
        return {
                'name': self.name,
                'creator': self.creator.username,
        }

    def url(self):
        return "/r/%s/" % self.name

    def __unicode__(self):
        return self.name

class Post(models.Model):
    url = models.CharField(max_length=1000)
    reddit_id = models.CharField(max_length=255, default="")
    title = models.CharField(max_length=1000)
    domain = models.CharField(max_length=255)
    is_self = models.BooleanField(default=False)
    author = models.ForeignKey(User, related_name='posts')
    score = models.IntegerField()
    body = models.TextField()
    sub = models.ForeignKey(Sub)
    scraped = models.BooleanField(default=False)

    def get_comments(self):
        cache_key = "post:%s" % self.id

        if cache_key in cache:
            return json.loads(cache.get(cache_key))

        children = list()
        for child in self.comments.all():
            children.append(child.agg())

        cache.set(cache_key, json.dumps(children))
        return children

    def dump(self):
        return {
                'url': self.url,
                'title': self.title,
                'author': {'username': self.author.username},
                'score': self.score,
                'body': self.body,
                'sub': self.sub.dump(),
        }

    def reddit_url(self):
        return "/r/%s/post/%s" % (self.sub.name, self.id)

    def sub_url(self):
        return "/r/%s/" % self.sub.name

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments')
    score = models.IntegerField()
    body = models.TextField()
    parent = models.ForeignKey('Comment', null=True, related_name='children')
    post = models.ForeignKey(Post, related_name='comments')
    scraped = models.BooleanField(default=False)

    def agg(self):
        children = list()
        for child in self.children.all():
            children.append(child.agg())

        tree = {
                'comment': self.dump(),
                'children': children,
        }

        return tree

    def dump(self):
        parent = None
        if self.parent:
            parent = self.parent.dump()

        return {
                'author': {'username': self.author.username},
                'score': self.score,
                'body': self.body,
                'parent': parent,
                'post': self.post.dump(),
            }

    def __unicode__(self):
        return self.author.username

class CommentVote(models.Model):
    author = models.ForeignKey(User)
    value = models.IntegerField()
    comment = models.ForeignKey(Comment, related_name='votes')

    def __unicode__(self):
        return "%s for %s" % (self.author.username, self.comment.id)

class PostVote(models.Model):
    author = models.ForeignKey(User)
    value = models.IntegerField()
    post = models.ForeignKey(Post, related_name='votes')

    def __unicode__(self):
        return "%s for %s" % (self.author.username, self.post.id)

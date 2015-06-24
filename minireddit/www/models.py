from django.db import models
from django.contrib.auth.models import User

class Sub(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='created_subs')
    subscribers = models.ManyToManyField(User, related_name='subscribed_to')

    def url(self):
        return "/r/%s/" % self.name

    def __unicode__(self):
        return self.name

class Post(models.Model):
    url = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User, related_name='posts')
    body = models.TextField()
    sub = models.ForeignKey(Sub)

    def get_comments(self):
        children = list()
        for child in self.comments.all():
            children.append(child.agg())
        return children

    def reddit_url(self):
        return "/r/%s/post/%s" % (self.sub.name, self.id)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments')
    score = models.IntegerField()
    body = models.TextField()
    parent = models.ForeignKey('Comment', null=True, related_name='children')
    post = models.ForeignKey(Post, related_name='comments')

    def agg(self):
        children = list()
        for child in self.children.all():
            children.append(child.agg())

        tree = {
                'comment': self,
                'children': children,
        }

        return tree

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

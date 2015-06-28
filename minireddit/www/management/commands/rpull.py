from django.core.management.base import BaseCommand, CommandError
from www.models import *
from django.core import serializers
import urllib
import urllib2
import json
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def read_json_page(url):
    print "requesting:", url
    time.sleep(5)
    aResp = urllib2.urlopen(url)
    return json.loads(aResp.read())

def create_or_get_user(username):
    try:
        return User.objects.get(username=username)
    except:
        return User.objects.create_user(
                username,
                "%s@foo.com" % username,
                "pass2"
            )

def create_or_get_sub(sub, creator=User.objects.get(username='root')):
    subreddit, created = Sub.objects.get_or_create(name=sub, defaults={'creator': creator})
    return subreddit

def handle_comment(post, node, parent=None):
    assert node['kind'] == 't1' or node['kind'] == 'more'

    if node['kind'] != 't1': 
        return

    data = node['data']
    author = data['author']
    score = data['score']
    body = data['body']
    author_user = create_or_get_user(author)

    current_comment = Comment.objects.create(
            author=author_user,
            score=score,
            body=body,
            parent=parent,
            post=post,
            scraped=True
        )

    if node['data']['replies']:
        children = node['data']['replies']['data']['children']
        for child in children:
            handle_comment(post, child, current_comment)

def read_comments(post, link):
    data = read_json_page(link)
    root_comments = data[1]['data']['children']
    for child in root_comments:
        handle_comment(post, child)

def read_sub(sub):
    data = read_json_page("http://reddit.com/r/%s/.json" % sub)
    children = data['data']['children']

    subreddit = create_or_get_sub(sub)

    for child in children:
        if child['kind'] == 't3':
            cdata = child['data']

            post = Post.objects.create(
                    url=cdata['url'],
                    title=cdata['title'],
                    author=create_or_get_user(cdata['author']),
                    score=cdata['score'],
                    body=cdata['selftext'],
                    sub=create_or_get_sub(sub),
                    scraped=True
            )

            """
            print cdata['domain']
            print cdata['url']
            print cdata['subreddit']
            print cdata['author']
            print cdata['title']
            print cdata['selftext']
            print cdata['selftext_html']
            print cdata['score']
            print cdata['permalink']
            print cdata['id']
            print
            """

            read_comments(post, "http://reddit.com%s.json" % cdata['permalink'])


class Command(BaseCommand):
    def handle(self, *args, **options):
        print read_sub('news')


from django.core.management.base import BaseCommand, CommandError
from www.models import *
from django.core import serializers
import urllib
import urllib2
import json
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def add_id_to_file(id):
    f = open("pulled", "a")
    f.write("%s\n" % id)
    f.close()

def read_json_page(url):
    print "requesting:", url
    while True:
        try:
            aResp = urllib2.urlopen(url)
            js = json.loads(aResp.read())
            print "fetched..."
            return js
        except:
            print "failed..."
            time.sleep(2)

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

def read_sub(sub, pulled):
    data = read_json_page("http://reddit.com/r/%s/.json" % sub)
    children = data['data']['children']

    subreddit = create_or_get_sub(sub)

    for child in children:
        if child['kind'] == 't3':
            cdata = child['data']

            if cdata['id'] in pulled:
                print 'skipping', cdata['id']
                continue

            """
            if Post.objects.filter(reddit_id=cdata['id']).exists():
                post = Post.objects.filter(reddit_id=cdata['id'])
                Comment.objects.filter(post=post).delete()
                post.delete()
            """

            post = Post.objects.create(
                    url=cdata['url'],
                    title=cdata['title'],
                    author=create_or_get_user(cdata['author']),
                    score=cdata['score'],
                    body=cdata['selftext'],
                    sub=create_or_get_sub(sub),
                    reddit_id=cdata['id'],
                    is_self=cdata['is_self'],
                    domain=cdata['domain'],
                    scraped=True
            )

            if cdata['is_self']:
                post.url = post.reddit_url()
                post.save()


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
            add_id_to_file(post.reddit_id)


class Command(BaseCommand):

    def handle(self, *args, **options):
        pulled = set()
        for line in open("pulled"):
            pulled.add(line.strip())

        to_pull = [
            #    'news', 
            #    'videos',
            #    'audiophile',
            #    'askreddit',
            #    'brewing',
            #    'linux',
            #    'movies',
            #    'truefilm',
            #    'wikipedia',
                'physics',
                'dailyprogrammer',
                'politics',
                'djent',
                'beer',
                'whatcouldgowrong',
                'crappydesign',
                'changemyview',
                ]
        for sub in to_pull:
            read_sub(sub, pulled)


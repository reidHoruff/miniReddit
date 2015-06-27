from django.template import RequestContext
from django.http import *
from sniper.snipers import *
import sniper.decorators as sniper
from easy.decorators import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from models import *
import forms

@sniper.ajax()
def register(request):
    form = forms.Register(request.POST)

    if not form.is_valid():
        yield InsertText('#error', form.get_first_error()), None

    if form.cleaned_data['password1'] != form.cleaned_data['password2']:
        yield InsertText('#error', "Passwords do not match"), None

    pw = form.cleaned_data['password1']

    try:
        username  = form.cleaned_data['username']
        email = '%s@foobar.com' % form.cleaned_data['username']

        user = User.objects.create_user(
            username,
            email,
            pw
        )
        user.save()

        user = authenticate(username=username, password=pw)

        login(request, user)
        yield RedirectBrowser('/'), None
    except:
        yield InsertText("#error", "Sorry, this username already exists :("), None

@sniper.ajax()
def submit(request):
    form = forms.SubmitPost(request.POST)

    if form.is_valid():
        title = form.cleaned_data['title']
        url = form.cleaned_data['url']
        subreddit = form.cleaned_data['subreddit']
        body = form.cleaned_data['body']

        if len(Sub.objects.filter(name=subreddit)) < 1:
            yield InsertText('#error', "subreddit not does not exist"), None

        post = Post.objects.create(
            url=url,
            title=title,
            author=request.user,
            body=body,
            sub=Sub.objects.get(name=subreddit)
        )
        yield RedirectBrowser('/r/%s/post/%s/' % (subreddit, post.id)), None

    else:
        yield InsertText('#error', form.get_first_error()), None

@sniper.ajax()
def comment(request):
    form = forms.PostComment(request.POST)

    if form.is_valid():
        body = form.cleaned_data['body']
        post_id = form.cleaned_data['post_id']
        parent_id = form.cleaned_data['parent_id']

        post = Post.objects.get(id=post_id)

        parent = None
        if parent_id >= 0:
            parent = Comment.objects.get(id=parent_id)

        Comment.objects.create(
            author=request.user,
            body=body,
            parent=parent,
            score=1,
            post=post
        )

        yield RedirectBrowser('/r/%s/post/%s/' % (post.sub.name, post.id)), None

    else:
        yield InsertText('#error', form.get_first_error()), None

@sniper.ajax()
def _logout(request):
    if request.user.is_authenticated():
        logout(request)
    n = request.REQUEST.get('next')
    if n:
        yield RedirectBrowser(n)
    else:
        yield RedirectBrowser('/')

@sniper.ajax()
def _login(request):
    form = forms.LoginForm(request.POST)

    if form.is_valid():
        username  = form.cleaned_data['username']
        email = '%s@foobar.com' % form.cleaned_data['username']
        pw = form.cleaned_data['password']
        user = authenticate(username=username, password=pw)

        if user and user.is_active:
            login(request, user)
            yield RedirectBrowser('/'), None

    yield InsertText("#error", "Error with login credentials"), None

@sniper.ajax()
def create_sub(request):
    form = forms.CreateSub(request.POST)

    if form.is_valid():
        name  = form.cleaned_data['name']
        if len(Sub.objects.filter(name=name)) > 0:
          yield InsertText('#error', 'sub name already exists'), None

        Sub.objects.create(name=name, creator=request.user)
        yield RedirectBrowser('/r/%s/' % name), None
    else:
        yield InsertText('#error', form.get_first_error()), None

@sniper.ajax()
def view_comment_reply(request):
    parent_id = request.REQUEST['parent_id']
    post_id = request.REQUEST['post_id']

    args = {
            'commentform': forms.PostComment().set_parent_id(parent_id).set_post_id(post_id),
    }

    yield InsertTemplate(".reply-box-%s"%parent_id, "replybox.html", args)

@sniper.ajax()
def vote(request):
    type = request.REQUEST.get('type')
    id = request.REQUEST.get('id')
    value = request.REQUEST.get('value')
    value = {'u': 1, 'd': -1}[value]

    if type == 'post':
        post = Post.objects.get(id=id)
        old_value = 0
        if PostVote.objects.filter(author=request.user, post=post).exists():
            vote = PostVote.objects.get(author=request.user, post=post)
            old_value = vote.value
            vote.value = value
            vote.save()
        else:
            PostVote.objects.create(
                    author=request.user,
                    post=post,
                    value=value
                    )
        post.score -= old_value
        post.score += value
        post.save()
        yield JSLog("score updated: %s" % post.score)
        yield InsertText("#score-%s" % id, post.score)

    if type == 'comment':
        comment = Comment.objects.get(id=id)
        old_value = 0
        if CommentVote.objects.filter(author=request.user, comment=comment).exists():
            vote = CommentVote.objects.get(author=request.user, comment=comment)
            old_value = vote.value
            vote.value = value
            vote.save()
        else:
            CommentVote.objects.create(
                    author=request.user,
                    comment=comment,
                    value=value
                    )
        comment.score -= old_value
        comment.score += value
        comment.save()
        yield JSLog("score updated: %s" % comment.score)

@sniper.ajax()
def sub(request):
    type = request.REQUEST.get('type')
    id = request.REQUEST.get('id')
    value = request.REQUEST.get('value')
    value = {'u': 1, 'd': -1}[value]

    if type == 'post':
        post = Post.objects.get(id=id)
        old_value = 0
        if PostVote.objects.filter(author=request.user, post=post).exists():
            vote = PostVote.objects.get(author=request.user, post=post)
            old_value = vote.value
            vote.value = value
            vote.save()
        else:
            PostVote.objects.create(
                    author=request.user,
                    post=post,
                    value=value
                    )
        post.score -= old_value
        post.score += value
        post.save()
        yield JSLog("score updated: %s" % post.score)
        yield InsertText("#score-%s" % id, post.score)

    if type == 'comment':
        comment = Comment.objects.get(id=id)
        old_value = 0
        if CommentVote.objects.filter(author=request.user, comment=comment).exists():
            vote = CommentVote.objects.get(author=request.user, comment=comment)
            old_value = vote.value
            vote.value = value
            vote.save()
        else:
            CommentVote.objects.create(
                    author=request.user,
                    comment=comment,
                    value=value
                    )
        comment.score -= old_value
        comment.score += value
        comment.save()
        yield JSLog("score updated: %s" % comment.score)

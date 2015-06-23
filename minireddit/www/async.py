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
        isroot = form.cleaned_data['isroot']
        postid = form.cleaned_data['postid']
        parent_id = form.cleaned_data['parent_id']

        parent = None
        if parent_id >= 0:
            parent = Comment.objects.get(id=parent_id)

        post = Comment.objects.create(
            author=request.user,
            body=body,
            parent=request.user,
            body=body,
            sub=Sub.objects.get(name=subreddit)
        )
        yield RedirectBrowser('/r/%s/post/%s/' % (subreddit, post.id)), None

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

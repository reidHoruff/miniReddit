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

  if len(pw) < 8 or len(pw) > 20:
    yield InsertText("#error", "Password must be between 8 and 20 characters long"), None

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
  form = forms.Register(request.POST)
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
      next = form.cleaned_data['next']
      if next:
        yield RedirectBrowser(next), None
      else:
        yield RedirectBrowser('/profile/'), None

  yield InsertText("#error", "Error with login credentials"), None

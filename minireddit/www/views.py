from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from easy.decorators import *
from www.models import *
import forms

@context_template_response
def home(request):
    data = {
            'form': forms.LoginForm(),
            'posts': Post.objects.all(),
            'is_sub': False,
            }
    return "home.html", data

def subreddit(request, subreddit):
    data = {
            'form': forms.LoginForm(),
            'posts': Post.objects.filter(sub=Sub.objects.get(name=subreddit)),
            'is_sub': True,
            'subreddit': subreddit,
            }

    return render_to_response(
            "home.html",
            data,
            context_instance=RequestContext(request)
        )

def view_post(request, subreddit, post_id):
    print Post.objects.get(id=post_id).get_comments()
    data = {
            'form': forms.LoginForm(),
            'post': Post.objects.get(id=post_id),
            'is_sub': True,
            'subreddit': subreddit,
            'rootcommentform': forms.PostComment().set_parent_id(-1).set_post_id(post_id),
            }

    return render_to_response(
            "post.html",
            data,
            context_instance=RequestContext(request)
        )

@context_template_response
def register(request):
    return "register.html", {'form': forms.Register()}

@context_template_response
def submit(request):
    sub = request.REQUEST.get('sub')
    return "submit.html", {'form': forms.SubmitPost().set_sub(sub)}

@context_template_response
def create_sub(request):
    return "createsub.html", {'form': forms.CreateSub()}

@context_template_response
def _login(request):
    return "login.html", {'form': forms.LoginForm()}

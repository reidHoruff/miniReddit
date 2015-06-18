from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from easy.decorators import *
from www.models import *
import forms

@context_template_response
def home(request):
  return "home.html", {}

@context_template_response
def register(request):
  return "register.html", {'form': forms.Register()}

@context_template_response
def submit(request):
  return "submit.html", {'form': forms.SubmitPost()}

@context_template_response
def _login(request):
  return "login.html", {'form': forms.LoginForm()}

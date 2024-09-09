from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.urls import reverse
#-----------------------VIEWS-------------------------
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'publico/home.html'

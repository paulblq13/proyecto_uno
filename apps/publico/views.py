from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

#-----------------------VIEWS-------------------------
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'publico/publico.html'

class Invitacion01View(TemplateView):
    template_name = 'publico/invitacion_01.html'    

class Invitacion02View(TemplateView):
    template_name = 'publico/invitacion_02.html'       

class EscritorioView(TemplateView):
    template_name = 'publico/escritorio.html'


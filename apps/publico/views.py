from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

#-----------------------VIEWS-------------------------
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'publico/publico.html'

class LoginView(TemplateView):
    template_name = 'publico/login.html'
    
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('inputUsernameLogin') 
        password = request.POST.get('inputPasswordLogin') 
        remember_me = request.POST.get('remember_me', False) 
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user) 
            # Configurar la duración de la sesión 
            if remember_me:
                request.session.set_expiry(5)  # 1 hora (3600 segundos)
            else:
                request.session.set_expiry(5)  # 20 minutos (1200 segundos)
            print("login OK")
            return HttpResponseRedirect(reverse('index'))
        else:
            print("login Fail")
            return render(request, 'publico/login.html', {'error': True})
    else:
        print("login Fail")
        return render(request, 'publico/login.html', {'error': False})

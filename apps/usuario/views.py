from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

#-----------------------VIEWS-------------------------
from django.views.generic import TemplateView

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
                request.session.set_expiry(28800)  # 1 hora
            else:
                request.session.set_expiry(28800)  # 20 minutos
            
            print("Login OK")
            return HttpResponseRedirect(reverse('index'))
        else:
            # Si la autenticación falla, volvemos al formulario con un mensaje de error
            print("Login Fail")
            return render(request, 'usuario/login.html', {'error': True})
    else:
        # En caso de método GET, mostramos el formulario de login
        return render(request, 'usuario/login.html', {'error': False})


class LoginView(TemplateView):
    template_name = 'usuario/login.html'


def logoutDef(request):
    logout(request)
    return redirect('index')  
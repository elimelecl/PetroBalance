from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.contrib.auth import logout as auth_logout
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

def usuarios(request):
    return render(request, "usuarios.html")

def home(request):
    return redirect('inventarios:movimientos')

class Login(auth_views.LoginView):
    template_name = 'usuario/login.html'
    redirect_field_name = "Prueba"
    def render_to_response(self, context, **response_kwargs):
        if self.request.user.username != '':
            return HttpResponseRedirect(reverse("home"))
        return super(Login, self).render_to_response(
            context, **response_kwargs
        )

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
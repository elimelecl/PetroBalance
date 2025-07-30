"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_ap|||import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_apPetroBalance.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    path('infrastructura/', include(('infrastructura.urls', 'infrastructura'), namespace='infrastructura')),
    path('inventarios/', include(('inventarios.urls', 'inventarios'), namespace='inventarios')),
    path('reportes/', include(('reportes.urls', 'reportes'), namespace='reportes')),
    path('', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

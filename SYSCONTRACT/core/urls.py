"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),  # Inclui as rotas do app login
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),  # Rota para a página de Início
    path('clientes/', include('clientes.urls')),
    path('suporte/', TemplateView.as_view(template_name='suporte.html'), name='suporte'),  # Rota para a página de Suporte
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('clientes/', TemplateView.as_view(template_name='clientes.html'), name='clientes'),
    path('contrato/', TemplateView.as_view(template_name='contrato.html'), name='contrato'),
    path('gerenciador/', TemplateView.as_view(template_name='gerenciador.html'), name='gerenciador'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('cadastro/', TemplateView.as_view(template_name='cadastro-clientes.html'), name='cadastro'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])  # Use STATICFILES_DIRS
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

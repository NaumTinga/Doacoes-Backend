"""
URL configuration for projectDoacoes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls.moeda_urls')),  # Include URLs for the moeda app
    # path('api/', include('api.urls.pais_urls')),  # Include URLs for the pais app
    # path('api/', include('api.urls.banco_urls')),  # Include URLs for the banco app
    # path('api/', include('rubricaEstado.urls')),
    path('api/', include('api.urls.urls')),
    # path('api/', include('api.urls.conta_central_urls')),
    # path('api/', include('coordenador.urls')),
]

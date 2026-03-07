"""
URL configuration for novulnerable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from novulnerable.settings.base import MEDIA_ROOT, MEDIA_URL, DEBUG

handler404 = 'conf.views.custom_404'
handler403 = 'conf.views.custom_403'

urlpatterns = [
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),

    path('', auth_views.LoginView.as_view(), name='login'),
    path("demo/", include("demo.urls")),
    path("conf/", include("conf.urls")),
    path("usuario/", include("usuario.urls")),
    path("equipo/", include("equipo.urls")),
    path("perfil/", include("perfil.urls")),
    path("campeonato/", include("campeonato.urls")),

    # se la cambia para mejorar la seguridad.
    path('nvadmin/', admin.site.urls),

    path('', include('django.contrib.auth.urls'))
]

# Configuración para servir archivos multimedia en desarrollo
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

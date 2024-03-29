"""mkforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from forum.views import IndexView
from django.conf import settings
from django.conf.urls.static import static

# On va utiliser include afin de 
# séparé les filchiers urls de chaque app, et l'inclure ici.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('forum/', include("forum.urls")),
    path('account/', include("users.urls")), ]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns=[path("__debug__/",include("debug_toolbar.urls")),]+urlpatterns

#Adding Media
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
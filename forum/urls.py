from django.urls import path
from . import views


appname = "forum_app"

urlpatterns = [
    path('index/',views.indexView.as_view(),name='index')
]

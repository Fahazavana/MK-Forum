from django.urls import path
from . import views


app_name = "forum_app"
urlpatterns = [
    path('index/', views.indexView.as_view(), name='index'),
    path('create/', views.createPost.as_view(), name='create'),
    path('read/<int:pk>/', views.readPost.as_view(), name='read')
]

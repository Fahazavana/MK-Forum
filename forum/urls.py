from django.urls import path
from . import views


app_name = "forum_app"
urlpatterns = [
    path('index/', views.indexView.as_view(), name='index'),
    path('create/', views.createPost.as_view(), name='create'),  # CREATE
    path('read/<int:pk>/', views.readPost.as_view(), name='read'),  # READ
    path('read/<int:pk>/update', views.updatePost.as_view(),
         name='update'),  # UPDATE
    path('read/<int:pk>/delete', views.deletePost.as_view(),
         name='delete'),  # DELETE
]

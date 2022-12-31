from django.urls import path
from . import views


app_name = "forum_app"
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('create/', views.CreatePost.as_view(), name='create'),  # CREATE
    path('read/<int:pk>/', views.ReadPost.as_view(), name='read'),  # READ
    path('read/<int:pk>/update', views.UpdatePost.as_view(),
         name='update'),  # UPDATE
    path('read/<int:pk>/delete', views.DeletePost.as_view(),
         name='delete'),  # DELETE
    path('read/<int:pk>/react/<str:reactionType>', views.reactOnPost,
         name='reaction'),
     path('read/<int:pk>/comment', views.commentPost,
         name='commenter'),
]

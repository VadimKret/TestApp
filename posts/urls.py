from django.urls import path
from posts import views
from posts.views import page_posts

urlpatterns = [
    path('page/', page_posts),
    path(" ", views.posts),
]

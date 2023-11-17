from django.urls import path
from posts.views import page_posts

urlpatterns = [
    path('page/', page_posts),
]

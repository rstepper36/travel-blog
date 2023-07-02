from django.urls import path
from .views import home, post_detail, add_post

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('add_post/', add_post, name='add_post'),
]

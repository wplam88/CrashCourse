"""Defines URL Patterns for blogs"""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # index
    path('', views.index, name='index'),
    # blogs
    path('blogs/', views.blogs, name='blogs'),
    # new blog
    path('new_blog/', views.new_blog, name='new_blog'),
    # view blog
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    # new post
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    # new blog
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
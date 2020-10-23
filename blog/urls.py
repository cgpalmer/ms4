from django.urls import path
from . import views

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('', views.blog_info, name='blogs'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail')
]

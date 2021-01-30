from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('404', views.view_404_page, name='404_page')
]

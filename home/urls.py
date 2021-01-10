from django.urls import path
from . import views

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('', views.index, name='home'),
    path('404', views.view_404_page, name='404_page')
]

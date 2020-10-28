from django.urls import path
from . import views

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('add/', views.add_review, name='add_review'),
]

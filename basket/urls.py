from django.urls import path
from . import views

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('edit/', views.edit_basket, name='edit_basket')
]

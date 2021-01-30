from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('edit/', views.edit_basket, name='edit_basket'),
    path('delete_item/<basket_item_id>/', views.delete_basket_item, name='delete_basket_item'),
    path('empty/', views.empty_basket, name='empty_basket')
]

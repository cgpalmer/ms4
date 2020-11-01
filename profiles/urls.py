from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('profile', views.new_profile, name='new_profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('profiles/<product_id>', views.add_content_for_download, name='add_content_for_download'),
    
]

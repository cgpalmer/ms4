from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('reviews', views.review_history, name='review_history'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
]

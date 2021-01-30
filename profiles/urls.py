from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('admin/', views.admin_profile, name='admin_profile_page'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('profile', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('download/<download_id>', views.counting_downloads, name='counting_downloads'),
    path('delete/<photo_id>', views.delete_user_photo, name='delete_user_photo'),
    path('upload/<int:product_id>/', views.image_upload, name='image_upload'),
    path('profile_upload/', views.image_upload_from_profile, name='image_profile_upload'),
]

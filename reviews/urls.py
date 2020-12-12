from django.urls import path
from . import views

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('add/<int:product_id>/', views.add_review, name='add_review'),
    path('edit/<int:r_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:r_id>/', views.delete_review, name='delete_review'),
]

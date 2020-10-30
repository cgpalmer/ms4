from django.urls import path
from . import views

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('add/', views.add_review, name='add_review'),
    path('reviews', views.review_history, name='review_history'),
    path('edit/<int:r_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:r_id>/', views.delete_review, name='delete_review'),
]

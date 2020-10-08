from django.urls import path
from . import views

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]

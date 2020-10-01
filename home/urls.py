from django.urls import path, views

# The path is empty so it goes to the root home page.
urlpatterns = [
    path('', views.index, name='home')
]

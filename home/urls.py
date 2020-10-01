from django.urls import path, views

urlpatterns = [
    path('', views.index, name='home')
]

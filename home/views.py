from django.shortcuts import render
from django.shortcuts import render, redirect, reverse


def index(request):
    # Returning the index page
    return render(request, 'home/index.html')


def view_404_page(request):
    return render(request, 'home/404_page.html')


def bad_request(request, *args, **kwargs):
    return render(request, 'home/404_page.html')

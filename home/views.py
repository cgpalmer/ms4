from django.shortcuts import render

# Create your views here.


def index(request):
    # Returning the index page
    return render(request, 'home')

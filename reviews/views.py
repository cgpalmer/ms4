from django.shortcuts import render

# Create your views here.

def add_review(request):
    template = "reviews/add_review.html"
    context = {}
    return render(request, template, context)

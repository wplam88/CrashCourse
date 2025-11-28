from django.shortcuts import render

def index(request):
    """The home page for meals."""
    return render(request, 'meals/index.html')

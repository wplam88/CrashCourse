from django.shortcuts import render

def index(request):
    """The Home Page for Pizzas"""
    return render(request, 'pizzas/index.html')

from django.shortcuts import render

# Create your views here.
# core/views.py


def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

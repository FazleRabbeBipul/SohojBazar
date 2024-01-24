from django.shortcuts import render

# Create your views here.
# core/views.py

from item.models import Category, Item

def index(request):
    items = Item.objects.filter(is_sold = False)[0:9]
    categories = Category.objects.all()

    return render(request, 'core/index.html',{
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')

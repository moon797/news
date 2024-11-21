from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import News, NewsCategory

# Create your views here.
def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {"news":news, "categories":categories}

    return render(request, 'index.html' , context)

def category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    news= News.objects.filter(new_cat=category).all()
    context = {'news':news, 'category':category }
    return render(request, 'category_new.html', context)

def new_page(request, pk):
    new = News.objects.get(id=pk)
    context = {'new':new}
    return render(request, 'new_page.html', context)



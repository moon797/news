from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .models import News, NewsCategory

# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        news = News.objects.all()
        categories = NewsCategory.objects.all()
        context = {'news':news , 'categories': categories}

        return render(request, 'index.html', context)
    return redirect('about')

def about(request):
    try:
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, 'about.html')
    except:
        return render(request, 'about.html')

def category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    news= News.objects.filter(new_cat=category).all()
    context = {'news':news, 'category':category }
    return render(request, 'category_new.html', context)

def new_page(request, pk):
    new = News.objects.get(id=pk)
    context = {'new':new}
    return render(request, 'new.html', context)


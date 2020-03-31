from django.shortcuts import render

from rango.models import Category, Page


def index(request):
    most_liked_categories = Category.objects.order_by('-likes')[:5]
    most_viewed_pages = Page.objects.order_by('-views')[:5]
    context_dict = {
        'most_liked_categories': most_liked_categories,
        'most_viewed_pages': most_viewed_pages
        }
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Rafael"}
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

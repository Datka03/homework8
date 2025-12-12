from django.shortcuts import render
from apps.settings.models import Settings


def index(request):
    settings = Settings.objects.latest("id")
    return render(request,'index.html',locals())

def contact(request):
    settings = Settings.objects.latest("id")
    return render(request, 'contact-us.html',locals())

def about(request):
    settings = Settings.objects.latest("id")
    return render(request, 'about.html',locals())

def gallery_masonry(request):
    settings = Settings.objects.latest("all")
    return render(request, 'gallery-masonry.html',locals())

def book_table(request):
    settings = Settings.objects.latest("id")
    return render(request, 'book-table.html',locals())

def book_table_option2(request):
    settings = Settings.objects.latest("id")
    return render(request, 'book-table-option2.html',locals())

def blog_single_post(request):
    settings = Settings.objects.latest("id")
    return render(request, 'blog-single-post.html',locals())

def blog_list(request):
    settings = Settings.objects.latest("id")
    return render(request, 'blog-list.html',locals())


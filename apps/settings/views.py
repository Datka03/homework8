from django.shortcuts import render
from apps.settings.models import Settings

# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    return render(request,'index.html',locals())

def contact(request):
    settings = Settings.objects.latest("id")
    return render(request, 'contact-us.html', locals())

def about(request):
    settings = Settings.objects.latest("id")
    return render(request, 'about.html', locals())

def gallery(request):
    settings = Settings.objects.latest("id")
    return render(request, 'gallery.html', locals())

def book_table(request):
    settings = Settings.objects.latest("id")
    return render(request, 'book-table.html', locals())

def blog_list(request):
    settings = Settings.objects.latest("id")
    return render(request, 'blog-list.html' , locals())

def blog_deteils(request):
    settings = Settings.objects.latest("id")
    return render(request, 'blog-deteils.html' , locals())

def menu(request):
    settings = Settings.objects.latest("id")
    return render(request, 'menu.html', locals())

def chef(request):
    settings = Settings.objects.latest("id")
    return render(request, 'chef.html', locals())
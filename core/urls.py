"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from apps.settings.views import index, contact, about, gallery, book_table, blog_list, blog_detail, menu_list, our_chef

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index-page"),
    path('contacts/', contact, name="contact-page"),
    path('about/', about, name="about-page"),
    path('gallery/', gallery, name="gallery-page"),
    path('book-table/', book_table, name="book-table-page"),
    path('blog/', blog_list, name="blog-list-page"),
    path('blog-deteils/', blog_detail, name="blog-detail-page"),
    path('menu/', menu_list, name="menu-page"),
    path('chef/', our_chef, name="chef-page"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
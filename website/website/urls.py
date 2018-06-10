"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from blog.views import BlogpostView, BlogpostDetailView, BlogpostCreateView, BlogpostEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', BlogpostView.as_view(), name='posts'),
    path('posts/<int:id>/', BlogpostDetailView.as_view(), name='posts-detail'),
    path('posts/create/', BlogpostCreateView.as_view(), name='posts-create'),
    path('posts/<int:id>/edit/', BlogpostEditView.as_view(), name='posts-edit'),
]

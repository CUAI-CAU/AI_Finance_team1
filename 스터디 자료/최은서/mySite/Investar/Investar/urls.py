"""Investar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import sys
import os
import django
from django.contrib import admin
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from hello import views
from django.urls import path, re_path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
from index import views as index_views
from balance import views as balance_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?P<name>[A-Z][a-z]*)$', views.sayHello),
    path('index/', index_views.main_view),
    path('balance/', balance_views.main_view)
]
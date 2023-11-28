"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from .views import index, market, adventure, buy_item, start_adventure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('market/', market, name='market'),
    path('adventure/', adventure, name='adventure'),
    path('buy_item/<int:item_id>/', buy_item, name='buy_item'),
    path('start_adventure/', start_adventure, name='start_adventure'),
]


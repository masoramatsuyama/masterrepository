"""master URL Configuration

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
from box import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/', views.TopView.as_view(), name='top'),
    path('artistlist/', views.ArtistlistView.as_view(), name='artistlist'),
    path('artistdetail/<int:pk>', views.ArtistDetailView.as_view(), name='artistdetail'),
    path('buy/<int:pk>', views.BuyView.as_view(), name='buy'),
    path('thankyou/', views.ThankyouView.as_view(), name='thankyou'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

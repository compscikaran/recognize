"""recognize URL Configuration

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
from django.conf.urls.static import static
import upload.views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',upload.views.home,name = 'home'),
    path('about/',upload.views.about,name = 'about'),
    path('upload/',upload.views.scan,name='scan'),
    path('verify/',upload.views.verify,name='verify'),
    path('register/',upload.views.registeruser,name='register'),
    path('login/',upload.views.loginuser,name='login'),
    path('signout/',upload.views.signoutuser,name='signout'),
    path('search/',upload.views.search,name='search'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



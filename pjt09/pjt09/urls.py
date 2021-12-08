"""pjt09 URL Configuration

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
from django.contrib import admin
from django.urls import path, include
#+static()추가할 때 불러올 2개
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main_page.urls')),
    path('admin/', admin.site.urls),
    # path('community/', include('community.urls')),
    path('accounts/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
    # AllAuth추가
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


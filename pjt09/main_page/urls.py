from django.urls import path
from . import views


urlpatterns = [
    # 추가
    path('', views.mainpage, name='mainpage'),
]

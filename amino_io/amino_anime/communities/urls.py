from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.community_list, name='list'),   # пока заглушка
    path('create/', views.community_create, name='create'),
    path('<int:pk>/', views.community_detail, name='detail'),
    path('<int:pk>/join/', views.community_join, name='join'),
]
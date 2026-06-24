from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.community_list, name='list'),
    path('create/', views.community_create, name='create'),
    path('<int:pk>/', views.community_detail, name='detail'),
    path('<int:pk>/join/', views.community_join, name='join'),
    path('<int:pk>/manage/', views.community_manage, name='manage'),
    path('<int:pk>/role/<int:user_id>/', views.community_set_role, name='set_role'),
]
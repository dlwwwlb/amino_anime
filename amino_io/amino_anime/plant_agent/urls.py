from django.urls import path
from . import views

app_name = 'plant_agent'

urlpatterns = [
    path('', views.plant_list, name='list'),
    path('new/', views.plant_create, name='create'),
    path('<int:pk>/', views.plant_detail, name='detail'),
]

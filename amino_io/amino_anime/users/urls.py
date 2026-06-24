from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('edit/', views.profile_edit, name='edit_profile'),
    path('<str:username>/', views.profile_view, name='profile'),
]
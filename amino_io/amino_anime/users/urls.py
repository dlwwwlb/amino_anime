from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('<str:username>/', views.profile_view, name='profile'),
    # позже можно добавить редактирование профиля: path('edit/', views.profile_edit, name='edit'),
]
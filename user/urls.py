from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('user_create', views.UserCreateView.as_view(), name='user_create')
]

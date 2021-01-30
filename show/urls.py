from django.urls import path
from . import views

app_name = "show"

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/post_delete', views.PostDelete.as_view(), name='delete'),
]

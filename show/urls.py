from django.urls import path
from . import views

app_name = "show"

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
    path('parts_create', views.PartsCreateView.as_view(), name='parts_create'),
    path('<int:pk>/post_delete', views.PostDelete.as_view(), name='delete'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup')
]

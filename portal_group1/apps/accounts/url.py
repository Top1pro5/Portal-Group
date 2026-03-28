from django.urls import path
from django.conf.urls.i18n import urlpatterns
from .views import home_view, SignUpView, profile_view, post_delete, post_detail, t_post_detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",home_view, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/',profile_view, name='profile_self'),
    path('profile/<str:username>/',profile_view, name='profile'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    path('postt/<int:pk>/', post_detail, name='t_post_detail'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ads', views.ads, name='ads'),
    path('upload', views.upload, name='upload'),
    path('info', views.info, name='info'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('accounts/login/', views.redirect_to_login, name='redirectLogin'),
]
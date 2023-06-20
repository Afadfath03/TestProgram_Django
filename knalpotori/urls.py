from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="beranda"),
    path("login/", views.login, name="login"),   
    path('mobil/', views.mobil, name="mobil"),
    path('motor/', views.motor, name="motor"),
    path('aksesoris/', views.aksesoris, name="aksesoris"),
    path('detail/', views.detail, name="detail"),
    path('registrasi/', views.registrasi, name="registrasi"),
    path('login/', views.login, name="login"),
    path('cart/', views.cart, name="cart")
]
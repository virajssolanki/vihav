from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/<email>', views.dashboard, name='dashboard'),
    path('console/', views.console, name='console'),
    path('withdraw/withdraw', views.withdraw, name='withdraw'),
]
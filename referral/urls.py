from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/<email>', views.dashboard, name='dashboard'),
    path('console/', views.console, name='console'),
]
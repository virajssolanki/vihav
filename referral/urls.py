from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('dashboard/<email>', views.dashboard, name='dashboard'),
    path('accept/<pk>', views.accept, name='accept'),
    path('edit_ref/<pk>', views.edit_ref, name='edit_ref'),
    path('delete/<pk>', views.delete, name='delete'),
    path('console/', views.console, name='console'),
    path('console/<rpk>/', views.console, name='console'),
    path('console/<wpk>', views.console, name='console'),
    path('all_requests/', views.all_req, name='all_req'),
    path('all_references/', views.all_ref, name='all_ref'),
    path('withdraw/withdraw', views.withdraw, name='withdraw'),
]
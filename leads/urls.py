from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_lead, name='create_lead'),
    path('success/', views.success, name='success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard-data/', views.dashboard_data, name='dashboard_data'),
]
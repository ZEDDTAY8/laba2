from django.urls import path
from . import views

app_name = 'sports_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('save-settings/', views.save_settings, name='save_settings'),
]
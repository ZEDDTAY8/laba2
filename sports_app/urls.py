from django.urls import path
from . import views

app_name = 'sports_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('save-settings/', views.save_settings, name='save_settings'),
    path('toggle-favorite-team/', views.toggle_favorite_team, name='toggle_favorite_team'),
    path('toggle-favorite-league/', views.toggle_favorite_league, name='toggle_favorite_league'),
]
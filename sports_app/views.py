from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib.parse import quote, unquote
import json

# Данные о командах
TEAMS = [
    {'id': 1, 'name': 'Зенит-Казань', 'sport': 'Волейбол', 'country': 'Россия', 'league': 'Суперлига'},
    {'id': 2, 'name': 'Перуджа', 'sport': 'Волейбол', 'country': 'Италия', 'league': 'Серия А1'},
    {'id': 3, 'name': 'Скра', 'sport': 'Волейбол', 'country': 'Польша', 'league': 'ПлюсЛига'},
    {'id': 4, 'name': 'Кузбасс', 'sport': 'Волейбол', 'country': 'Россия', 'league': 'Суперлига'},
    {'id': 5, 'name': 'Трентино', 'sport': 'Волейбол', 'country': 'Италия', 'league': 'Серия А1'},
    {'id': 6, 'name': 'Лейкерс', 'sport': 'Баскетбол', 'country': 'США', 'league': 'НБА'},
    {'id': 7, 'name': 'ЦСКА', 'sport': 'Баскетбол', 'country': 'Россия', 'league': 'Единая лига ВТБ'},
    {'id': 8, 'name': 'Барселона', 'sport': 'Баскетбол', 'country': 'Испания', 'league': 'Евролига'},
    {'id': 9, 'name': 'Зенит', 'sport': 'Баскетбол', 'country': 'Россия', 'league': 'Единая лига ВТБ'},
    {'id': 10, 'name': 'Макаби', 'sport': 'Баскетбол', 'country': 'Израиль', 'league': 'Евролига'},
    {'id': 11, 'name': 'Реал Мадрид', 'sport': 'Футбол', 'country': 'Испания', 'league': 'Ла Лига'},
    {'id': 12, 'name': 'Челси', 'sport': 'Футбол', 'country': 'Англия', 'league': 'АПЛ'},
    {'id': 13, 'name': 'Бавария', 'sport': 'Футбол', 'country': 'Германия', 'league': 'Бундеслига'},
    {'id': 14, 'name': 'Зенит', 'sport': 'Футбол', 'country': 'Россия', 'league': 'РПЛ'},
    {'id': 15, 'name': 'ПСЖ', 'sport': 'Футбол', 'country': 'Франция', 'league': 'Лига 1'},
    {'id': 16, 'name': 'Старшая Карасуно', 'sport': 'Волейбол', 'country': 'Япония', 'league': 'Фикшн'},
    {'id': 17, 'name': 'Старшая Некома', 'sport': 'Волейбол', 'country': 'Япония', 'league': 'Фикшн'},
    {'id': 18, 'name': 'Старшая Инаризаки', 'sport': 'Волейбол', 'country': 'Япония', 'league': 'Фикшн'},
    {'id': 19, 'name': 'Bastard München', 'sport': 'Футбол', 'country': 'Япония', 'league': 'Фикшн'},
    {'id': 20, 'name': 'Ubers', 'sport': 'Футбол', 'country': 'Япония', 'league': 'Фикшн'},
    {'id': 21, 'name': 'Manshine City', 'sport': 'Футбол', 'country': 'Япония', 'league': 'Фикшн'}
]

# Данные о лигах
LEAGUES = [
    {'id': 1, 'name': 'Суперлига', 'sport': 'Волейбол'},
    {'id': 2, 'name': 'Серия А1', 'sport': 'Волейбол'},
    {'id': 3, 'name': 'ПлюсЛига', 'sport': 'Волейбол'},
    {'id': 4, 'name': 'НБА', 'sport': 'Баскетбол'},
    {'id': 5, 'name': 'Единая лига ВТБ', 'sport': 'Баскетбол'},
    {'id': 6, 'name': 'Евролига', 'sport': 'Баскетбол'},
    {'id': 7, 'name': 'Ла Лига', 'sport': 'Футбол'},
    {'id': 8, 'name': 'АПЛ', 'sport': 'Футбол'},
    {'id': 9, 'name': 'Бундеслига', 'sport': 'Футбол'},
    {'id': 10, 'name': 'РПЛ', 'sport': 'Футбол'},
    {'id': 11, 'name': 'Лига 1', 'sport': 'Футбол'},
    {'id': 12, 'name': 'Фикшн', 'sport': 'Разный'}
]

def index(request):
    # Декодируем списки любимых команд и лиг из cookies
    favorite_teams = json.loads(unquote(request.COOKIES.get('favorite_teams', '[]')))
    favorite_leagues = json.loads(unquote(request.COOKIES.get('favorite_leagues', '[]')))
    theme = request.COOKIES.get('theme', 'light')
    
    # Отображаемые названия для темы и языка
    theme_display = 'Светлая' if theme == 'light' else 'Тёмная'
    
    context = {
        'teams': TEAMS,
        'leagues': LEAGUES,
        'favorite_teams': favorite_teams,
        'favorite_leagues': favorite_leagues,
        'theme': theme,
        'theme_display': theme_display,
    }
    return render(request, 'sports_app/index.html', context)

def save_settings(request):
    if request.method == 'POST':
        response = redirect('sports_app:index')
        
        # Сохраняем тему и язык
        theme = request.POST.get('theme', 'light')
        response.set_cookie('theme', theme, max_age=365*24*60*60)
        
        return response
    return redirect('sports_app:index')

def toggle_favorite_team(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        favorite_teams = json.loads(unquote(request.COOKIES.get('favorite_teams', '[]')))
        
        if team_name in favorite_teams:
            favorite_teams.remove(team_name)
        else:
            favorite_teams.append(team_name)
        
        response = redirect('sports_app:index')
        response.set_cookie('favorite_teams', quote(json.dumps(favorite_teams)), max_age=365*24*60*60)
        return response
    return redirect('sports_app:index')

def toggle_favorite_league(request):
    if request.method == 'POST':
        league_name = request.POST.get('league_name')
        favorite_leagues = json.loads(unquote(request.COOKIES.get('favorite_leagues', '[]')))
        
        if league_name in favorite_leagues:
            favorite_leagues.remove(league_name)
        else:
            favorite_leagues.append(league_name)
        
        response = redirect('sports_app:index')
        response.set_cookie('favorite_leagues', quote(json.dumps(favorite_leagues)), max_age=365*24*60*60)
        return response
    return redirect('sports_app:index')
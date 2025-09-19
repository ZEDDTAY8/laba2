from django.shortcuts import render, redirect
from django.http import HttpResponse

# Данные о командах
TEAMS = [
    # Волейбол
    {'id': 1, 'name': 'Зенит-Казань', 'sport': 'Волейбол', 'country': 'Россия', 'league': 'Суперлига'},
    {'id': 2, 'name': 'Перуджа', 'sport': 'Волейбол', 'country': 'Италия', 'league': 'Серия А1'},
    {'id': 3, 'name': 'Скра', 'sport': 'Волейбол', 'country': 'Польша', 'league': 'ПлюсЛига'},
    {'id': 4, 'name': 'Кузбасс', 'sport': 'Волейбол', 'country': 'Россия', 'league': 'Суперлига'},
    {'id': 5, 'name': 'Трентино', 'sport': 'Волейбол', 'country': 'Италия', 'league': 'Серия А1'},
    
    # Баскетбол
    {'id': 6, 'name': 'Лейкерс', 'sport': 'Баскетбол', 'country': 'США', 'league': 'НБА'},
    {'id': 7, 'name': 'ЦСКА', 'sport': 'Баскетбол', 'country': 'Россия', 'league': 'Единая лига ВТБ'},
    {'id': 8, 'name': 'Барселона', 'sport': 'Баскетбол', 'country': 'Испания', 'league': 'Евролига'},
    {'id': 9, 'name': 'Зенит', 'sport': 'Баскетбол', 'country': 'Россия', 'league': 'Единая лига ВТБ'},
    {'id': 10, 'name': 'Макаби', 'sport': 'Баскетбол', 'country': 'Израиль', 'league': 'Евролига'},
    
    # Футбол
    {'id': 11, 'name': 'Реал Мадрид', 'sport': 'Футбол', 'country': 'Испания', 'league': 'Ла Лига'},
    {'id': 12, 'name': 'Челси', 'sport': 'Футбол', 'country': 'Англия', 'league': 'АПЛ'},
    {'id': 13, 'name': 'Бавария', 'sport': 'Футбол', 'country': 'Германия', 'league': 'Бундеслига'},
    {'id': 14, 'name': 'Зенит', 'sport': 'Футбол', 'country': 'Россия', 'league': 'РПЛ'},
    {'id': 15, 'name': 'ПСЖ', 'sport': 'Футбол', 'country': 'Франция', 'league': 'Лига 1'},

    # Фикшн
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
    {'id': 12, 'name': 'Фикшн', 'sport': 'Разный'},
]

def index(request):
    # Получаем настройки из cookies
    favorite_team = request.COOKIES.get('favorite_team', 'Не выбрана')
    favorite_league = request.COOKIES.get('favorite_league', 'Не выбрана')
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    
    context = {
        'teams': TEAMS,
        'leagues': LEAGUES,
        'favorite_team': favorite_team,
        'favorite_league': favorite_league,
        'theme': theme,
        'language': language,
    }
    return render(request, 'sports_app/index.html', context)

def save_settings(request):
    if request.method == 'POST':
        response = redirect('sports_app:index')
        
        # Сохраняем настройки в cookies
        response.set_cookie('favorite_team', request.POST.get('favorite_team'), max_age=365*24*60*60)
        response.set_cookie('favorite_league', request.POST.get('favorite_league'), max_age=365*24*60*60)
        response.set_cookie('theme', request.POST.get('theme'), max_age=365*24*60*60)
        response.set_cookie('language', request.POST.get('language'), max_age=365*24*60*60)
        
        return response

# Create your views here.

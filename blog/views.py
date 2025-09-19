from django.shortcuts import render, redirect
from django.utils.translation import activate, get_language
from django.http import HttpResponse

def index(request):
    courses = [
        {'title': 'Python для начинающих', 'duration': '8 недель'},
        {'title': 'Веб-разработка на Django', 'duration': '10 недель'},
    ]
    
    # Получаем настройки из cookies или используем значения по умолчанию
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    
    # Активируем выбранный язык
    activate(language)
    
    if request.method == 'POST':
        # Сохранение настроек в cookies
        response = redirect('index')
        response.set_cookie('theme', request.POST.get('theme', 'light'))
        response.set_cookie('language', request.POST.get('language', 'ru'))
        return response
    
    return render(request, 'courses/index.html', {
        'courses': courses,
        'theme': theme,
        'language': language
    })
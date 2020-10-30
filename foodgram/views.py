from django.shortcuts import render


def author(request):
    """Страница об исполнителе проекта"""

    headline = 'Об авторе'
    text = 'Кирилл Антонов - начинающий Python-разработчик.'

    return render(request, 'about.html', {
        'text': text,
        'headline': headline})


def tech(request):
    """Страница о технологиях, используемых в проекте"""

    headline = 'Технологии'
    text = 'Django, PostgreSQL, YandexCloud, Docker, Nginx.'

    return render(request, 'about.html', {
        'text': text,
        'headline': headline})


def page_not_found(request, exception):
    """Ошибка 404"""
    return render(request, '404.html', {'path': request.path}, status=404)


def server_error(request):
    """Ошибка 500"""
    return render(request, '500.html', {'path': request.path}, status=500)

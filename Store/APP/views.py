from django.shortcuts import render

def index (request):
    data = {
        'title' : 'Главная страница',
        'values' : ['some', 'Hello', '123']
    }
    return render (request, 'app/index.html', data)

def about(request):
    return render (request, 'app/about.html')
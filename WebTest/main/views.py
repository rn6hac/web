from django.shortcuts import render
def index(request):
    data = {                           #Создание словаря
        'title': 'Главная страница',
        'values': ['some', 'hello', '123']  #Массив
    }
    return render(request, 'main/index.html', data) #Передача функции index.html и передача шаблонов списками

def about(request):
    return render(request, 'main/about.html')


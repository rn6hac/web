from django.urls import path
from. import views

urlpatterns = [
   path('', views.index, name='home'), #Задаем имя переменной гланой страницы
   path('about', views.about, name='about'), #Задаем имя переменной О нас
]
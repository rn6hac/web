from django.urls import path
from. import views

urlpatterns = [
   path('', views.news_home, name='news_home'), #Задаем имя переменной гланой страницы
   path('create', views.create, name='create'), #Задаем имя переменной гланой страницы
   path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail') #Отслеживание динамических параметров
]
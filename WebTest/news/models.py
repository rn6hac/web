from django.db import models

class Articles(models.Model): # Создание БД на основе модели класса
    title = models.CharField('Название', max_length=50) #Поле не больше 255 символов
    anons = models.CharField('Анонс', max_length=250)  # Поле не больше 255 символов
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:                                #Создаем класс для задания другого имени таблицы в панели джанго
               verbose_name = 'Новость'
               verbose_name_plural = 'Новости'

"""Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
"""

from django.db import models
from django.urls import NoReverseMatch, reverse
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    title = models.CharField(max_length=100, unique=True)
    custom_url = models.CharField(max_length=50, null=True, blank=True)
    url_name = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_url(self):
        if self.url_name:
            try:
                return reverse(self.url_name)
            except NoReverseMatch:
                return "#"
        elif self.custom_url:
            return self.custom_url
        else:
            return "#"
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



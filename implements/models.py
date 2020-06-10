from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категория"""

    title = models.CharField(max_length=50, verbose_name='Название категории')
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение категории')
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Color(models.Model):
    """Цвет"""

    title = models.CharField(max_length=50, verbose_name='Название цвета')
    image = models.ImageField(upload_to='colors/', verbose_name='Изображение цвета')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Element(models.Model):
    """Элемент"""

    title = models.CharField(max_length=50, verbose_name='Элемент')
    image = models.ImageField(upload_to='elements/', verbose_name='Изображение элемента')
    count = models.SmallIntegerField(verbose_name='Количество')
    purchase_price = models.SmallIntegerField(verbose_name='Закупочная цена')
    price = models.SmallIntegerField(verbose_name='Цена продажи')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория элемента')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name='Цвет')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
        ordering = ['title']
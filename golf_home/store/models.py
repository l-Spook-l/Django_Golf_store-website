from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# from uuid import uuid4
# import pathlib
# from django.contrib.auth.models import User


# уникально имя фото
# def photo_directory_and_name(instance, filename):
#     filepath = pathlib.Path(filename)
#     new_filename = uuid4()
#     return f'photos/product/{new_filename}{filepath.suffix}'


# удалять картинки из папки при удалении продукт
class Product(models.Model):
    """Продукты магазина"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.IntegerField()
    rating = models.IntegerField(default=0)
    """для картинки нужно доп. модуль (pip install Pillow")"""
    photo = models.ImageField(upload_to='photos/product/')
    # photo = models.ImageField(upload_to=photo_directory_and_name)  # уникально имя фото
    """Ключ указываем где много, 
        on_delete=models.PROTECT - запрещаем удалять тип если есть хотя бы 1 продукт этого типа """
    type = models.ForeignKey('TypeProduct', on_delete=models.PROTECT)  # 1 тип (one to many)
    brand = models.ForeignKey('BrandProduct', on_delete=models.PROTECT)  # 1 брэнд (one to many)
    time_create = models.DateTimeField(auto_now_add=True)  # принимаем текущее время и не меняется

    def __str__(self):
        return self.name

    # фун-я для получения нужного - url, так же при использовании классов, помогает перенаправить на нужную стр.
    # урок - 8, помогает в админ-панели сгенерировать кнопку (смотреть на сайте)
    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    # авто формирование слага
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    # при удалении продукта, удалять из папки фото
    def delete(self, *args, **kwargs):
        # Удаляем файл, связанный с этой записью
        self.photo.delete()
        super().delete(*args, **kwargs)

    # для настройки в админ-панели
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['time_create', 'name']  # сортировка везде


class TypeProduct(models.Model):
    """Тип продукта, первичная модель"""
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    # для настройки в админ-панели
    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'
        ordering = ['name']  # сортировка везде

    def get_absolute_url(self):
        # type -  название в URL (name='type')
        return reverse('type', kwargs={'type_slug': self.slug})


class BrandProduct(models.Model):
    """Производитель продукта, первичная модель"""
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/brand/')
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

    # для настройки в админ-панели
    class Meta:
        verbose_name = 'Брэнд продукта'
        verbose_name_plural = 'Брэнды продуктов'
        ordering = ['name']  # сортировка везде

    def get_absolute_url(self):
        # brand -  название в URL (name='brand')
        return reverse('brand', kwargs={'brand_slug': self.slug})


"""For next versions"""
# class InfoProduct(models.Model):
#     product = models.ForeignKey('Product', on_delete=models.PROTECT)
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.title

# class Basket(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#
# # продукт в корзине
# class BasketProduct(models.Model):
#     basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
#     product = models.OneToOneField('Product', on_delete=models.CASCADE)


# в другую модель class Rating(models.Model):
#     user = models.IntegerField()
#     product = models.IntegerField()
#     grade = models.IntegerField()

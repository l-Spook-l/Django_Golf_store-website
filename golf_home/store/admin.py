from django.contrib import admin
from .models import Product, TypeProduct, BrandProduct

"""
is_superuser - просмотр инфо в админ-панели
is_staff - доступ к админ-панели"""


# название как правило соападает с нужной моделью
class ProductAdmin(admin.ModelAdmin):
    # список полей которые мы хотим видеть в админ-панеле
    # list_display = ('id', 'name', 'time_create', 'photo', 'is_published')
    list_display = ('id', 'name', 'slug', 'price', 'rating', 'photo', 'time_create')
    # клик по этим поляем позволяет перейти на нужную статью
    list_display_links = ('id', 'name')
    # делаем поле редактируемым
    # list_editable = ('is_published',)
    # поля по которым можно будет делать фильтрацию (появляется фильтр справа)
    # list_filter = ('is_published', 'time_create')
    # по каким полям делать поиск
    search_fields = ('name',)
    # автозаполнение слага на основе имени, урок-12
    prepopulated_fields = {'slug': ('name',)}


class TypeProductAdmin(admin.ModelAdmin):
    # список полей которые мы хотим видеть в админ-панеле
    # list_display = ('id', 'name', 'time_create', 'photo', 'is_published')
    list_display = ('id', 'name', 'slug')
    # клик по этим поляем позволяет перейти на нужную статью
    list_display_links = ('id', 'name')
    # делаем поле редактируемым
    # list_editable = ('is_published',)
    # поля по которым можно будет делать фильтрацию (появляется фильтр справа)
    # list_filter = ('is_published', 'time_create')
    # по каким полям делать поиск
    search_fields = ('name',)
    # автозаполнение слага на основе имени, урок-12
    prepopulated_fields = {'slug': ('name',)}


class BrandProductAdmin(admin.ModelAdmin):
    # список полей которые мы хотим видеть в админ-панеле
    # list_display = ('id', 'name', 'time_create', 'photo', 'is_published')
    list_display = ('id', 'name', 'slug', 'photo')
    # клик по этим поляем позволяет перейти на нужную статью
    list_display_links = ('id', 'name')
    # делаем поле редактируемым
    # list_editable = ('is_published',)
    # поля по которым можно будет делать фильтрацию (появляется фильтр справа)
    # list_filter = ('is_published', 'time_create')
    # по каким полям делать поиск
    search_fields = ('name',)
    # автозаполнение слага на основе имени, урок-12
    prepopulated_fields = {'slug': ('name',)}


#
#
# class InfoProductAdmin(admin.ModelAdmin):
#     # список полей которые мы хотим видеть в админ-панеле
#     # list_display = ('id', 'name', 'time_create', 'photo', 'is_published')
#     list_display = ('id', 'title', 'slug')
#     # клик по этим поляем позволяет перейти на нужную статью
#     list_display_links = ('id', 'title')
#     # делаем поле редактируемым
#     # list_editable = ('is_published',)
#     # поля по которым можно будет делать фильтрацию (появляется фильтр справа)
#     # list_filter = ('is_published', 'time_create')
#     # по каким полям делать поиск
#     search_fields = ('name',)
#     # автозаполнение слага на основе имени, урок-12
#     prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(TypeProduct, TypeProductAdmin)
admin.site.register(BrandProduct, BrandProductAdmin)
# admin.site.register(InfoProduct, InfoProductAdmin)

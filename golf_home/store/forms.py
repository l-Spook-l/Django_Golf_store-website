from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddProductForm(forms.ModelForm):
    # конструктор класса
    def __init__(self, *args, **kwargs):
        # вызов конструктора базового класса
        super().__init__(*args, **kwargs)
        # для поля (type, brand) меняем св-во (empty_label)
        self.fields['type'].empty_label = 'Категория не выбрана'
        self.fields['brand'].empty_label = 'Категория не выбрана'

    # name = forms.CharField(label='Name',
    #                        widget=forms.TextInput(attrs={'class': 'form-input'}))
    # price = forms.IntegerField(label='Price',
    #                         widget=forms.IntegerField(attrs={'class': 'form-input'}))

    # photo = forms.ImageField(label='Photo',
    #                          widget=forms.ImageField(attrs={'class': 'form-input'}))

    class Meta:
        # связь формы с нужной моделью
        model = Product
        # какие поля отобразить в форме, кроме автозаполнения (__all__)
        # fields = '__all__'
        fields = ['name', 'price', 'photo', 'type', 'brand']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-input'}),
            'type': forms.Select(attrs={'class': 'form-input'}),
            'brand': forms.Select(attrs={'class': 'form-input'}),
        }

    # свой валидатор (проверка), должен начинаться с (clean_), даль для какого поля (name)
    def clean_name(self):
        # получаем данные по ключу (name)
        name = self.cleaned_data['name']
        # если длинна меньше 10 символов, вызываем исключение
        if len(name) < 10:
            # генерируем исключение
            raise ValidationError('Длинна меньше 10  символов')
        return name

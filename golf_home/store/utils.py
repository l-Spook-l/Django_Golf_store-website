"""Утилиты"""
from .models import BrandProduct, TypeProduct


class DataMixin():
    def get_user_context(self, **kwargs):
        context = kwargs
        brands = BrandProduct.object.all()
        types = TypeProduct.objects.all()
        context['brands'] = brands
        context['types'] = types
        return context

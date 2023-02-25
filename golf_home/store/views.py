from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from os import remove

from .models import *
from .forms import AddProductForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# from .utils import DataMixin


class StoreHome(ListView):
    model = TypeProduct
    template_name = 'store/index.html'
    context_object_name = 'types_products'

    def get_context_data(self, *, object_list=None, **kwargs):
        # берем уже существующий контекст (это словарь), на основе класса - ListView
        context = super().get_context_data(**kwargs)
        brands_products = BrandProduct.objects.all()
        # types_products = TypeProduct.objects.all()
        context['brands_products'] = brands_products
        # context['types_products'] = types_products
        return context


# =======================================================================================
class TypeShow(ListView):
    model = Product
    template_name = 'store/type.html'
    context_object_name = 'type_product'
    # если в списке нету записей, будет вызвана - 404
    allow_empty = False
    paginate_by = 12  # количество элементов на 1й стр (18 урок)

    def get_context_data(self, *, object_list=None, **kwargs):
        # берем уже существующий контекст (это словарь), на основе класса - ListView
        context = super().get_context_data(**kwargs)
        # w = Product.objects.filter(type__slug='type_slug')
        context['type'] = self.kwargs['type_slug']
        return context

    def get_queryset(self):
        return Product.objects.filter(type__slug=self.kwargs['type_slug'])


# {% url 'type' type.slug %}
# =======================================================================================
class BrandShow(ListView):
    model = Product
    template_name = 'store/brand.html'
    context_object_name = 'brand_product'
    # если в списке нету записей, будет вызвана - 404
    allow_empty = False
    paginate_by = 12  # количество элементов на 1й стр (18 урок)

    def get_context_data(self, *, object_list=None, **kwargs):
        # берем уже существующий контекст (это словарь), на основе класса - ListView
        context = super().get_context_data(**kwargs)
        context['brand'] = self.kwargs['brand_slug']
        return context

    def get_queryset(self):
        return Product.objects.filter(brand__slug=self.kwargs['brand_slug'])


# {% url 'brand' brand.slug %}
# =======================================================================================
class ProductShow(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'product'
    # по-умолчанию этот метода будет искасть просто по - slug (в URL - <slug:slug>), название можно любое
    slug_url_kwarg = 'product_slug'


# =======================================================================================
class AddProduct(CreateView):
    form_class = AddProductForm
    template_name = 'store/addproduct.html'
    query_pk_and_slug = True
    success_url = reverse_lazy('store_home')


# =======================================================================================
class UpdateProduct(UpdateView):
    model = Product
    template_name = 'store/addproduct.html'
    slug_url_kwarg = 'product_slug'

    fields = ['name', 'price', 'type', 'brand']


# =======================================================================================
class DeleteProduct(ListView, DeleteView):
    model = Product
    template_name = 'store/deleteProduct.html'
    success_url = reverse_lazy('store_home')
    slug_url_kwarg = 'product_slug'

    # remove(f'static/images/{product_delete.name_image}')
    # def get_queryset(self):
    #     print(Product.objects.filter(slug=self.kwargs['product_slug']))
    # return Product.objects.filter(slug=self.kwargs['brand_slug'])


# =======================================================================================
class ProfileUser(LoginRequiredMixin, ListView):
    model = Product
    # model = User
    template_name = 'store/profile.html'
    # context_object_name = 'user'
    # pk_url_kwarg = 'pk'


# =======================================================================================
# обработчик страницы 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>HZ</h1>')

# def page_not_found(request, exception):
#     return render(request, '404.html', status=404)

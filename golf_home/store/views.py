from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import *
from .forms import AddProductForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class StoreHome(ListView):
    model = TypeProduct
    template_name = 'store/index.html'
    context_object_name = 'types_products'

    def get_context_data(self, *, object_list=None, **kwargs):
        # берем уже существующий контекст (это словарь), на основе класса - ListView
        context = super().get_context_data(**kwargs)
        brands_products = BrandProduct.objects.all()
        context['brands_products'] = brands_products
        return context


# {% url 'type' type.slug %}
class TypeShow(ListView):
    model = Product
    template_name = 'store/type.html'
    context_object_name = 'type_product'
    # если в списке нету записей, будет вызвана - 404
    allow_empty = False
    paginate_by = 12  # количество элементов на 1й стр

    def get_context_data(self, *, object_list=None, **kwargs):
        # берем уже существующий контекст (это словарь), на основе класса - ListView
        context = super().get_context_data(**kwargs)
        context['type'] = \
            Product.objects.filter(type__slug=self.kwargs['type_slug']).values('type__name')[0]['type__name']

        return context

    def get_queryset(self):
        return Product.objects.filter(type__slug=self.kwargs['type_slug'])


# {% url 'brand' brand.slug %}
class BrandShow(ListView):
    model = Product
    template_name = 'store/brand.html'
    context_object_name = 'brand_product'
    # если в списке нету записей, будет вызвана - 404
    allow_empty = False
    paginate_by = 12  # количество элементов на 1й стр

    def get_context_data(self, *, object_list=None, **kwargs):
        # берем уже существующий контекст (это словарь), на основе класса - ListView
        context = super().get_context_data(**kwargs)
        context['brand'] = \
            Product.objects.filter(brand__slug=self.kwargs['brand_slug']).values('brand__name')[0]['brand__name']
        # при таком запросе получаем напр(Adidas - как бренд, и можем получить тип каждого товара
        # print(Product.objects.filter(brand__slug=self.kwargs['brand_slug']).values('type__name'))
        return context

    def get_queryset(self):
        return Product.objects.filter(brand__slug=self.kwargs['brand_slug'])


class ProductShow(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'product'
    # по-умолчанию этот метод будет искать просто по - slug (в URL - <slug:slug>), название можно любое
    slug_url_kwarg = 'product_slug'


class AddProduct(LoginRequiredMixin, CreateView):
    form_class = AddProductForm
    template_name = 'store/addproduct.html'
    query_pk_and_slug = True
    success_url = reverse_lazy('store_home')


class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'store/addproduct.html'
    slug_url_kwarg = 'product_slug'
    # можно только что-то одно, или form_class или fields
    form_class = AddProductForm
    # какие поля можно обновить
    # fields = ['name', 'price', 'rating', 'photo', 'type', 'brand']


class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'store/deleteProduct.html'
    success_url = reverse_lazy('store_home')
    slug_url_kwarg = 'product_slug'


class ProfileUser(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'store/profile.html'


# обработчик страницы 404
def page_not_found(request, exception):
    return render(request, 'store/page_404.html', status=404)

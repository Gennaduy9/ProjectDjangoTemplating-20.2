from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from carapp.forms import ProductForm
from carapp.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all()[:0],
        'title': 'Автомобильный салон - Главная',
        'lending': 'Кредитование - Мечтайте смелее',
        'Online': 'Покупка онлайн',
        'description': 'Cведения, представленные на сайте, носят информационный характер и не являются публичной офертой',
        'Search': 'Поиск'
    }
    return render(request, 'carapp/index.html', context)

def categorys(request):
    context = {
        'object_list': Category.objects.all(),
        'description': 'Машина должна быть частью тебя, а ты — её составной частью. Только так можно стать единственным в своем роде. Лучшая машина — новая машина!'

    }
    return render(request, 'carapp/categorys.html', context)


def contacts(request):
    return render(request, 'carapp/contacts.html')


def connection(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'carapp/connection.html')

def blog(request):
    return render(request, 'carapp/blog.html')

def privacy(request):
    return render(request, 'carapp/privacy.html')

def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Модель автомобиля - {category_item.name}'
    }
    return render(request, 'carapp/products.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)  # Показывать 10 продуктов на странице
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'product_list.html', {'products': products})
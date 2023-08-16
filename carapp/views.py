import random

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify


from carapp.models import Category, Product, Blog


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

def store(request):
    return render(request, 'carapp/store.html')

def privacy(request):
    return render(request, 'carapp/privacy.html')

def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk)[:1],
        'title': f'Модель автомобиля - {category_item.name}'
    }
    return render(request, 'carapp/products.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'carapp/includes/inc_product.html'
    context_object_name = 'object'
    pk_url_kwarg = 'pk'


class ProductListView(ListView):
    model = Product
    template_name = 'carapp/includes/inc_product.html'
    context_object_name = 'object_list'
    paginate_by = 10



class BlogListView(ListView):
    model = Blog
    template_name = 'blog/includes/inc_entry_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/entry_detail.html'
    context_object_name = 'object'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content')
    context_object_name = 'object'
    template_name = 'blog/entry_form.html'

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        slug = slugify(new_blog.title)
        if Blog.objects.filter(slug=slug).exists():
            # Запись с таким же значением slug уже существует
            # Вам нужно выполнить соответствующие действия здесь, например, добавить случайное число к slug
            slug += str(random.randint(1, 1000))
        new_blog.slug = slug
        new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('carapp:entry_delete', kwargs={'slug': self.object.slug})


class BlogUpdateView(UpdateView):
    model = Blog

    template_name = 'blog/entry_form.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'  # URL, на который перенаправлять после успешного удаления
    template_name = 'blog/entry_confirm_delete.html'





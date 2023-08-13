from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    color = models.CharField(max_length=50, **NULLABLE, verbose_name='Цвет')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    updated = models.DateTimeField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category}) - {self.price} руб.'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

# class Blog(models.Model):
#     title = models.CharField(max_length=250, verbose_name='Заголовок')
#     slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
#     content = models.TextField(**NULLABLE, verbose_name='Содержимое')
#     preview = models.ImageField(upload_to='blog_previews/', **NULLABLE, verbose_name='Превью')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     is_published = models.BooleanField(default=False, verbose_name='Признак публикации')
#     view_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
#
#     def __str__(self):
#         return f'{self.title}'
#
#     class Meta:
#         verbose_name = "Запись блога"
#         verbose_name_plural = "Записи блога"

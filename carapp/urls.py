from django.urls import path

from carapp.apps import CarappConfig
from carapp.views import index, categorys, contacts, connection, blog, category_products, create_product, product_list, \
    privacy

app_name = CarappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categorys/', categorys, name='categorys'),
    path('contacts/', contacts, name='contacts'),
    path('connection/', connection, name='connection'),
    path('blog/', blog, name='blog'),
    path('<int:pk>/products/', category_products, name='category_products'),
    path('products/', product_list, name='product_list'),
    path('privacy/', privacy, name='privacy'),
    path('create/', create_product, name='create_product')
]
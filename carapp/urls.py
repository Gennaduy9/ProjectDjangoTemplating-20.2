from django.urls import path

from carapp import views
from carapp.apps import CarappConfig
from carapp.views import index, categorys, category_products, contacts, connection, store, \
    privacy, ProductDetailView, BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CarappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categorys/', categorys, name='categorys'),
    path('<int:pk>/products/', category_products, name='category_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('contacts/', contacts, name='contacts'),
    path('connection/', connection, name='connection'),
    path('store/', store, name='store'),
    path('privacy/', privacy, name='privacy'),
    path('blog/', BlogListView.as_view(), name='entry_list'),
    path('blog/create/', BlogCreateView.as_view(), name='entry_form'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='entry_detail'),
    path('blog/<slug:slug>/update/', BlogUpdateView.as_view(), name='entry_update'),
    path('blog/<slug:slug>/delete/', BlogDeleteView.as_view(), name='entry_delete'),

]
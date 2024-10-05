from django.urls import path
from .views import MainView, CatalogView, search_view, add_to_order, view_order, update_order_item, delete_order_item, place_order, order_history, advanced_search, ProductDetailView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('search/', search_view, name='search_view'),
    path('add_to_order/<int:product_id>/', add_to_order, name='add_to_order'),
    path('order/', view_order, name='view_order'),
    path('update_order_item/<int:item_id>/', update_order_item, name='update_order_item'),
    path('delete_order_item/<int:item_id>/', delete_order_item, name='delete_order_item'),
    path('place_order/', place_order, name='place_order'),
    path('order_history/', order_history, name='order_history'),
    path('advanced_search/', advanced_search, name='advanced_search'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

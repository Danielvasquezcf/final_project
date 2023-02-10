from django.urls import path, include
from products.views import create_product, list_products, list_categories, CategoryUpdateView, CategoryDeleteView, ProductDeleteView, ProductUpdateView, CategoryCreateView

urlpatterns = [
     
    path('create-product/', create_product),
    
    path('list-products/', list_products),
    
    path('list-categories/', list_categories, name='categories'),

    path('update-product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),

    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

    path('create-category/', CategoryCreateView.as_view(), name='create_category'),
    
    path('delete-category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

    path('update-category/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),


]

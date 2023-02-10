from django.urls import path
from providers.views import ProviderListView, ProviderCreateView, ProviderDeleteView,ProviderUpdateView

urlpatterns = [
    path('providers-list/', ProviderListView.as_view(), name='providers_list'),

    path('create-provider/', ProviderCreateView.as_view(), name='create_provider'),

    path('update-provider/<int:pk>/', ProviderUpdateView.as_view(), name='update_provider'),
    
    path('delete-provider/<int:pk>/', ProviderDeleteView.as_view(), name='delete_provider'),
]
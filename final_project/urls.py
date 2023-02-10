
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from final_project.views import  index, about



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    
    path('products/', include('products.urls')), 

    path('providers/', include('providers.urls')),
    
    path('users/', include('users.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

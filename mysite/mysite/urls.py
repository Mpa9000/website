from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('historias/', include('internetstories.urls')),
    path('paginas/', include('allpages.urls')),
    path('contact/', include('contact.urls')),
    path('home/', include('home.urls')),
    path('entrar/', include('register.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('', include('redirect.urls')),
]

from django.contrib import admin
from django.urls import path, include
from pwa import urls as pwa_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Atestados.urls')),
    path('pwa/', include(pwa_urls)),
] 

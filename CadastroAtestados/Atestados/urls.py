from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('cadastrar/', views.cadastrar_atestado, name='cadastrar_atestado'),
    path('lista/', views.lista_atestados, name='lista_atestados'),
    path('inicio/', views.inicio, name='inicio'),
    path('', views.inicio, name='inicio'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
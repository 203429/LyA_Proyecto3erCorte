from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^api/potencia', include('conjunto_potencia.urls')),
    re_path(r'^api/operaciones/', include('operaciones.urls') ),
    re_path(r'^api/notacion/', include('notacion.urls') ),
]

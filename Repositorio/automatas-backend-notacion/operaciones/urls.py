from django.urls import re_path

from operaciones.views import OperacionesView

urlpatterns = [
    re_path(r'^ejercicio/', OperacionesView.as_view()),
]
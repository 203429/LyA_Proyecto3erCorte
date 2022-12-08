from django.urls import re_path

from conjunto_potencia.views import Example

urlpatterns = [
    re_path('/', Example.as_view()),
]
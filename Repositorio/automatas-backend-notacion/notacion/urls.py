from django.urls import path, re_path
from django.conf.urls import include

from notacion.views import Calculo, Quiz

urlpatterns = [
    re_path(r'verificar', Calculo.as_view()),  
    re_path(r'quiz', Quiz.as_view()),   
]
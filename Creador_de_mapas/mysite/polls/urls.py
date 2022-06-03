from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # el view.index es una funcion de python
]

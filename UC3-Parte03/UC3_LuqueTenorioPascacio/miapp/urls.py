from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path('', views.home, name='home'),
    path('examen/', views.examen, name='examen'),
]
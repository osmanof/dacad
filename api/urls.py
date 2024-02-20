from django.urls import path, include

from . import views

urlpatterns = [
    path('etwas', views.answer),
]


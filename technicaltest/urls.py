from django.urls import path

from . import views

urlpatterns = [
    path('', views.technicaltest, name='Technical Test'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('protected-journey-63770.herokuapp.com', views.index, name='index'),
    ''
]

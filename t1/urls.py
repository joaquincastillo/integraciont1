from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name="protected-journey-63770.herokuapp.com/"),
    ''
]
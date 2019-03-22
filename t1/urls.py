from django.urls import path, re_path


from . import views

urlpatterns = [
    re_path('protected-journey-63770.herokuapp.com',views.index),
    path('', views.index, name='index'),
]
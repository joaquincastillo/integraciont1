from django.urls import path, re_path


from . import views

urlpatterns = [
    path('t1/', views.index, name='index'),
]
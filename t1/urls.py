from django.urls import path, re_path


from . import views

urlpatterns = [
    path('t1/', views.index, name='index'),
    path('film/<url_param>/', views.show_film_page, name='film_page')
]
    #path(r'film/^(?P<url_param>\S+/$', views.show_film_page, name='film_page')
]

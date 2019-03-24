from django.urls import path, re_path


from . import views

urlpatterns = [
    path('t1/principal_page.html', views.index, name='index'),
    path(r'film/^(?P<url_param>[\w-S]+/$', views.show_film_page, name='film_page')
]

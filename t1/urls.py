from django.urls import path, re_path


from . import views

urlpatterns = [
    path('t1/', views.index, name='index'),
    path(r't1/film/', views.show_film_page, name='film_page'),
    path(r't1/character/', views.show_character_page, name='character_page'),
    path(r't1/planet/', views.show_planet_page, name='planet_page'),
    path(r't1/starship/', views.show_starship_page, name='starship_page'),
    path(r't1/search/', views.show_search_page, name='search_page')
]
    #path('film/<url_param>/', views.show_film_page, name='film_page')
#]
#    path(r'film/^(?P<url_param>\S+/$', views.show_film_page, name='film_page')


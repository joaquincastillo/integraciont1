from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from urllib3 import PoolManager
import json
import certifi


# Create your views here.


def index(request):
    url = "https://swapi.co/api/films/"
    #return HttpResponse("Hello, world. You're at the t1 index.")
    http = PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
    r = http.request('GET', url)
    print(r.status)

    # Decode UTF-8 bytes to Unicode, and convert single quotes
    # to double quotes to make it valid JSON
    my_json = r.data.decode('utf8')
    print(my_json)
    print('- ' * 20)

    # Load the JSON to a Python list & dump it back out as formatted JSON
    films = json.loads(my_json)
    # Para ver el json como string bonito
    # json_films = json.dumps(films, indent=4, sort_keys=True)
    # print(json_films)

    # --------- Requisito NAV 1 ---------- #
    # Para la página principal
    film_dict = {}
    for film in films["results"]:
        title = film["title"]
        year = film["release_date"]
        director = film["director"]
        producer = film["producer"]
        episode = film["episode_id"]
        url = film["url"]
        pos = url.find("films")
        small_url = url[pos+6:len(url)-1]
        film_dict[episode] = {"title": title, "year": year, "director": director,
                              "producer": producer, "episode": episode, "url": url,
                              "small_url": small_url}

    return render(request, 'principal_page.html', {'films': film_dict})


def show_film_page(request):
    url_param = request.GET.get("url_param")
    req_url = "https://swapi.co/api/films/{}".format(url_param)

    # return HttpResponse("Hello, world. You're at the t1 index.")
    http = PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
    r = http.request('GET', req_url)
    my_json = r.data.decode('utf8')
    film = json.loads(my_json)

    # Obteniendo info de los personajes
    characters = {}
    for character_url in film["characters"]:
        char_req = http.request('GET', character_url)
        char_json = char_req.data.decode('utf8')
        character = json.loads(char_json)
        char_name = character["name"]
        char_url = character["url"]
        pos = char_url.find("people")
        url_id = character["url"][pos+7:len(character["url"])-1]
        characters[url_id] = char_name

    # Obteniendo info de las starships
    starships = {}
    for ship_url in film["starships"]:
        ship_req = http.request('GET', ship_url)
        ship_json = ship_req.data.decode('utf8')
        ship = json.loads(ship_json)
        ship_name = ship["name"]
        s_url = ship["url"]
        pos = s_url.find("people")
        url_id = ship["url"][pos + 10:len(ship["url"]) - 1]
        starships[url_id] = ship_name

    # Obteniendo info de los planetas
    planets = {}
    for planet_url in film["planets"]:
        planet_req = http.request('GET', planet_url)
        planet_json = planet_req.data.decode('utf8')
        planet = json.loads(planet_json)
        planet_name = planet["name"]
        p_url = planet["url"]
        pos = p_url.find("planets")
        url_id = planet["url"][pos + 8:len(planet["url"]) - 1]
        planets[url_id] = planet_name

    return render(request, 'film_page.html', {"film": film, "characters": characters,
                                              "starships": starships, "planets": planets})

def show_character_page(request):
    url_param = request.GET.get("url_param")
    req_url = "https://swapi.co/api/people/{}".format(url_param)
    http = PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
    r = http.request('GET', req_url)
    my_json = r.data.decode('utf8')
    character = json.loads(my_json)

    render(request, 'character_page.html', {"character": character})






from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from urllib3 import PoolManager
import json
import certifi
url = "https://swapi.co/api/films/"


# Create your views here.


def index(request):
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
        film_dict[episode] = {"title": title, "year": year, "director": director,
                          "producer": producer, "episode": episode}

    return render(request, 'principal_page.html', {'films':films})





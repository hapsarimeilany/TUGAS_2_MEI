from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_mywatchlist(request):
    data_film_watchlist = WatchList.objects.all()

    data_film_watched = []
    data_film_not_watched = []

    for film in data_film_watchlist:
        if film.watched == "Watched":
            data_film_watched.append(film)
        else:
            data_film_not_watched.append(film)        

    total_watched = len(data_film_watched)
    total_not_watched = len(data_film_not_watched)
    pesan = ""

    if total_watched >= total_not_watched:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"
    

    context = {
        'list_film': data_film_watchlist,
        'nama': 'Meilany',
        'NPM': '2106751436',
        'pesan': pesan,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

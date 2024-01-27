from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from movies.models import Worker


# Create your views here.
def index(request):
    all_workers = Worker.objects.all()
    return render(request, 'index.html', {"data": all_workers})


def category(request, cat_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Категория: </h1><p>{cat_id}<p>")


def archive(request, year):
    if int(year) > 2024:
        raise Http404()
    return HttpResponse(f"<h1>Архив: </h1><p>{year}<p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

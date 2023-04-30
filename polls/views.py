from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def counter(request):
    textCount = len(request.GET["text"].split())
    print(textCount)
    return render(request, "counter.html", {"count":textCount})


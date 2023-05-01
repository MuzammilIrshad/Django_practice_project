from django.shortcuts import render
from django.http import HttpResponse
from .models import Vote

def index(request):
    votes = Vote.objects.all()
    print(votes)
    return render(request, "index.html",{"votes":votes})

def counter(request):
    textCount = len(request.POST["text"].split())
    print(textCount)
    return render(request, "counter.html", {"count":textCount})


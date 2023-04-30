from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
       "name":"Muzammil irshad",
       "age":25,
       "isMale":True
    }
    return render(request, "index.html", context)


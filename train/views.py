from django.http import HttpResponse
from django.shortcuts import render

def index(request) :
    return render(request, "train/index.html", {
        "username" : "client",
        "email" : "client.train@example.com",
    })

def show(request, title) :
    return render(request, "train/show.html", {
        title : "SNCF",
    })

def create(request) :
    return render(request, "train/create.html", {})

def login(request) :
    return render(request, "train/login.html", {})

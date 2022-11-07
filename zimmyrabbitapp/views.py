from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Welcome!')

def create(request):
    return HttpResponse('Creat')

def read(requestm,id):
    return HttpResponse('Read'+id)


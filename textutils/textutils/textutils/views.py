# I have created this file - Shivam
from django.http import HttpResponse
from django.shortcuts import render

import urllib.request

def sh(request):
    return HttpResponse(urllib.request.urlopen("google.com").read())

def index(request):
    params = {'name': 'Shivam', 'place': 'India'}
    return render(request,"index.html",params)



def removepunc(request):
    #Get the text
    djtext=request.GET.get('text','default')
    print(djtext)
    #Analyze the text
    return HttpResponse("Removed Punctuation <a href='/'>back</a>")


def capfirst(request):
    return HttpResponse("Capitalized First Letter <a href='/'>back</a>")

def newlineremove(request):
    return HttpResponse("Removed Newlines <a href='/'>back</a>")


def spaceremove(request):
    return HttpResponse("Removed Spaces <a href='/'>back</a>")


def charcount(request):
    return HttpResponse("Character Count <a herf='/'>back</a>")


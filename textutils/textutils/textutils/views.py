# I have created this file - Shivam
from django.http import HttpResponse
import urllib.request
def sh(request):
    return HttpResponse(urllib.request.urlopen("https://github.com/imshivamchoudhary").read())

def index(request):
    return HttpResponse("Home")



def removepunc(request):
    return HttpResponse("Removed Punctuation")


def capfirst(request):
    return HttpResponse("Capitalized First Letter")

def newlineremove(request):
    return HttpResponse("Removed Newlines")


def spaceremove(request):
    return HttpResponse("Removed Spaces")


def charcount(request):
    return HttpResponse("Character Count")`


# I have created this file - Shivam
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

import urllib.request
def sh(request):
    return HttpResponse(urllib.request.urlopen("https://github.com/imshivamchoudhary").read())
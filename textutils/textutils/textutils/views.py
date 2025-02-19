# I have created this file - Shivam
from django.http import HttpResponse
from django.shortcuts import render

# import urllib.request
#
# def sh(request):
#     return HttpResponse(urllib.request.urlopen("google.com").read())

def index(request):
    params = {'name': 'Shivam', 'place': 'India'}
    return render(request,"index.html",params)



def analyze(request):
    #Get the text
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    punctuations='''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    # analyzed=djtext
    if removepunc=='on':
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        #Analyze the text
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('error')

#
# def capfirst(request):
#     return HttpResponse("Capitalized First Letter ")
#
# def newlineremove(request):
#     return HttpResponse("Removed Newlines")
#
#
# def spaceremove(request):
#     return HttpResponse("Removed Spaces ")
#
#
# def charcount(request):
#     return HttpResponse("Character Count ")


# I have created this files - AG

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    #Checkboxes values
    removepunc = request.POST.get('removepunc', 'off');
    fullcap = request.POST.get('fullcap', 'off');
    fullsmall = request.POST.get('fullsmall', 'off');
    swapcase = request.POST.get('swapcase', 'off');
    title = request.POST.get('title', 'off');
    spaceremove = request.POST.get('spaceremover', 'off');
    extraspaceremove = request.POST.get('extraspaceremover', 'off');
    newlineremove = request.POST.get('newlineremover', 'off');
    print(djtext)
    # Analyze the text
    if removepunc == 'on':
        analyzed = rempun(djtext)
        purpose = 'Remove Punctuation'
        djtext = analyzed
    if (fullcap == 'on'):
        analyzed = djtext.upper()
        purpose = 'Captalize String'
        djtext = analyzed
    if (fullsmall == 'on'):
        analyzed = djtext.lower()
        purpose = 'Lower String'
        djtext = analyzed
    if (swapcase == 'on'):
        analyzed = djtext.swapcase()
        purpose = 'Swap Case'
        djtext = analyzed
    if title == 'on':
        analyzed = djtext.title()
        purpose = 'Captalize first character of each word'
        djtext = analyzed
    if spaceremove == 'on':
        analyzed = spacerem(djtext)
        purpose = 'Remove Spaces'
        djtext = analyzed
    if newlineremove == 'on':
        analyzed = newlineremover(djtext)
        purpose = 'Remove new line'
        djtext = analyzed
    if extraspaceremove == 'on':
        analyzed = extraspaceremover(djtext)
        purpose = 'Extra Space Remover'
        djtext = analyzed
    if(removepunc == 'off' and fullcap == 'off'and fullsmall == 'off' and swapcase == 'off' and title == 'off' and spaceremove == 'off' and newlineremove == 'off' and extraspaceremove == 'off'):
        analyzed = djtext
        purpose = 'Do Nothing with text'
        
    params = {'purpose': purpose, 'analyzed_text':analyzed}
    return render(request, 'analyze.html', params)

def rempun(text):
    punctuations = '''!()-[]{};:'"\|/?<>,.@#$%^&*_+`~='''
    analyzed=""
    for char in text:
        if char not in punctuations:
            analyzed = analyzed + char
    return analyzed

def spacerem(text):
    space = " "
    analyzed=""
    for char in text:
        if char not in space:
            analyzed = analyzed + char
    return analyzed

def newlineremover(text):
    analyzed = ""
    for char in text:
        if char !='\n' and char != '\r':
            analyzed = analyzed + char
    return analyzed

def extraspaceremover(text):
    analyzed = ""
    for index, char in enumerate(text):
        if not(text[index] == " " and text[index+1] == " "):
            analyzed = analyzed + char
    return analyzed

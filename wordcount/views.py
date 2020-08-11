import operator
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html", {"snacks": "pistachio"})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    textlength = len(wordlist)

    worddict = {}

    for word in wordlist:
        if word == "-":
            textlength -= 1
        else:
            if word in worddict:
                worddict[word] += 1
            else:
                worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
                
    return render(request, "count.html", {"fulltext": fulltext, "textlength": textlength, "sortedwords": sortedwords})
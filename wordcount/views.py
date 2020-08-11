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
        scrap_chars = "!.?,;:\"'{}[]()/"
        for char in scrap_chars:
            word = word.replace(char, "")

        lword = word.lower()

        if lword == "-":
            textlength -= 1
        else:
            if lword in worddict:
                worddict[lword] += 1
            else:
                worddict[lword] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
                
    return render(request, "count.html", {"fulltext": fulltext, "textlength": textlength, "sortedwords": sortedwords})
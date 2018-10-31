from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'Home.htm')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key= operator.itemgetter(1), reverse=True )
    return render(request, 'count.htm', {'fulltext': fulltext,
     'lenght':len(wordlist), 'sortedwords':worddictionary})

def about(request):
    return render(request, 'about.htm')
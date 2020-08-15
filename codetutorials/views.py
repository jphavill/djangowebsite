from django.shortcuts import render

def ifElse(request):
    return render(request, 'codetutorials/if-Else-Statement.html')

def tuples(request):
    return render(request, 'codetutorials/tuples.html', {'section': 'tuples'})


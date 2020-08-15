from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def articles(request):
    return render(request, 'main/articles.html')

def data(request):
    return render(request, 'main/data.html')
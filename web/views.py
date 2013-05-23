from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html', {'content':'Welcome to The Pineapple Project'})

def about(request):
    return render(request, 'web/about.html')

def join(request):
    return render(request, 'web/join.html')
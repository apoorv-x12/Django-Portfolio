from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'main/index.html',context)

def projects(request):
    context={}
    return render(request,'main/projects.html',context)

def languages(request):
    context={}
    return render(request,'main/languages.html',context)


def books(request):
    context={}
    return render(request,'main/books.html',context)
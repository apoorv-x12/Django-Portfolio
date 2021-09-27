from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    name=settings.DATA['NAME']
    about_me=settings.DATA1['ABOUT_ME']
    context={'name':name, "about_me":about_me}
    return render(request,'main/index.html',context)

def projects(request):
    projects=settings.DATA['PROJECTS']
    context={'projects':projects}
    return render(request,'main/projects.html',context)

def languages(request):
    languages=settings.DATA1['LANGUAGES']
    context={'languages':languages}
    return render(request,'main/languages.html',context)


def books(request):
    books_summary=settings.DATA['BOOKS_SUMMARY']
    context={"books_summary":books_summary}
    return render(request,'main/books.html',context)
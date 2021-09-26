from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('projects/',views.projects,name='projects'),
    path('languages/',views.languages,name='languages'),
    path('books/',views.books,name="books"),
]

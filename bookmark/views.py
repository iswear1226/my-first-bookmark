from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.

#--- ListView
class BookmarkLV(ListView) :
    model = Bookmark

#--- DetailView
class BookmarkDV(DetailView) :
    model = Bookmark
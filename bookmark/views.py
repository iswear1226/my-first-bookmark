from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.
# 클래스형 제네릭 뷰를 사용하기 위한 임포트
from django.views.generic import ListView,DetailView
# 모델 클래스 임포트
from bookmark.models import Bookmark

#--- ListView
class BookmarkLV(ListView) :
    model = Bookmark

#--- DetailView
class BookmarkDV(DetailView) :
    model = Bookmark
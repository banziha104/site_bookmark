from django.shortcuts import render
from django.views.generic import  ListView,DetailView,CreateView,DeleteView,UpdateView #리스트뷰와 디테일뷰를 불러옮
from .models import Bookmark


# 컨트롤러의 역할을 함

class BookmarkListV(ListView): # 장고에서 미리 준비되어있는 리스트뷰를 사용함
    model = Bookmark

class BookmarkDetailV(DetailView): # 장고에서 미리 준비되어있는 디테일뷰를 사용함
    model = Bookmark

class BookmarkCreateV(CreateView):
    model = Bookmark
    fields = ['title','url']

class BookmarkDeleteV(DeleteView):
    model = Bookmark

class BookmarkUpdateV(UpdateView):
    model = Bookmark

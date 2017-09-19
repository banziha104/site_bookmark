from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import  ListView,DetailView,CreateView,DeleteView,UpdateView #리스트뷰와 디테일뷰를 불러옮
from .models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin # 이걸 상속받으면, 어드민 권한만실행가능
# 컨트롤러의 역할을 함

class BookmarkListV(ListView): # 장고에서 미리 준비되어있는 리스트뷰를 사용함
    model = Bookmark

class BookmarkDetailV(DetailView): # 장고에서 미리 준비되어있는 디테일뷰를 사용함
    model = Bookmark

class BookmarkCreateV(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('bookmark:index') # rediction

    def form_valid(self, form): # 장입
        form.instance.author_id = self.request.user.id # user 클래스의 id를 넣어줌

        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark/')
        else :
            return self.render_to_response({'form':form})

class BookmarkDeleteV(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')  # rediction

class BookmarkUpdateV(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index') # rediction
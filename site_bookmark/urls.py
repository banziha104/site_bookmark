from django.conf.urls import url, include
from django.contrib import admin
from .views import IndexPage

# 라우팅을 담당하는 부분
urlpatterns = [
    url(r'^$', IndexPage.as_view(), name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include("bookmark.urls", namespace="bookmark")), # namespace를 지정함으로써 식별할 수 있음
]

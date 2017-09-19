from django.conf.urls import url, include
from django.contrib import admin

# 라우팅을 담당하는 부분
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include("bookmark.urls"))
]

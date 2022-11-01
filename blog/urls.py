from django.urls import path
# 장고 함수인 path 와 blog 애플리케이션에서 사용할 모든 views 를 import함(가져옴)
from . import views
# 첫 번째 URL 패턴을 추가
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
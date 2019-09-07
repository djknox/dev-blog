from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<str:slug>/', views.post_detail, name="post-detail"),
    path('tags/<str:slug>/', views.tag_detail, name="tag-detail"),
]
from django.urls import path

from .router import views

urlpatterns = [
    path('', views.index),
    path('post', views.post, name="post"),
    path('post_result', views.post_result, name="post_result"),
    path('post_detail', views.post_detail, name="post_detail"),
    path('file_upload/', views.upload_image_form, name="file_upload"),
]
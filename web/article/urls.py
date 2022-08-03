from django.urls import path

from .router import views

urlpatterns = [
    path('', views.index),
    path('post', views.post, name="post"),
    path('post_result', views.post_result, name="post_result"),
    path('file_upload/', views.upload_image_form, name="file_upload"),
]
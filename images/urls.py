from django.urls import path, include
from . import views

app_name = 'images'
urlpatterns = [
    path('', views.images_list, name="list"),
    path('<slug:slug>', views.image_page, name="page"),
    path('upload/', views.image_upload, name="upload"),
]
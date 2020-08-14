from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('diff_1', views.diff_1, name='diff_1'),
    path('diff_2', views.diff_2, name='diff_2'),
    path('diff_3', views.diff_3, name='diff_3'),
    path('ajax', views.ajax, name='ajax'),
]
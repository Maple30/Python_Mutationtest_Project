from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    path('diff_1', views.diff_1, name='diff_1'),
    path('diff_1/<str:bangou>/', views.diff_1, name='diff_1_get'),
    path('diff_2', views.diff_2, name='diff_2'),
    path('diff_3', views.diff_3, name='diff_3'),
    path('ajax', views.ajax, name='ajax'),
    path('tool', views.tool_download, name='tool_download'),
    path('diff_1_load', views.diff_1_load, name='diff_1_load'),
    path('diff_2_load', views.diff_2_load, name='diff_2_load'),
    path('diff_3_load', views.diff_3_load, name='diff_3_load'),
]
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='homepage'),
    path('Articles/', views.articles, name='articles'),
    path('Data/', views.data, name='data')
]

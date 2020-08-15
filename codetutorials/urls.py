from django.urls import path
from . import views

app_name = 'tut'
urlpatterns = [
    path('If-Else/', views.ifElse, name='tut-if-Else'),
    path('Tuples/', views.tuples, name='tut-tuples'),

]
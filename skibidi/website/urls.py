from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='index'),
        path('<str:anime>/<int:stagione>/<int:ep>',views.anime, name='anime')
]

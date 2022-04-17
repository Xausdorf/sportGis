from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('map', views.map, name='map'),
    path('info', views.info, name='info'),
]
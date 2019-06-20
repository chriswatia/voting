from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='votes-index'),
    path('', views.home, name='votes-home'),
    path('about/', views.about, name='votes-about')
]



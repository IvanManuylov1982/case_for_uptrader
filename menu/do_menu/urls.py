from django.urls import path

from . import views

#app_name = 'do_menu'


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<str:category>/', views.index, name='category'),
]

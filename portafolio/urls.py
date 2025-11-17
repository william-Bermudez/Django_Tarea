from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('william.html', views.william, name='william'),
    path('victor.html', views.victor, name='victor'),
    path('emely.html', views.emely, name='emely'),
    path('nelson.html', views.nelson, name='nelson'),
    path('franklin.html', views.franklin, name='franklin'),
]

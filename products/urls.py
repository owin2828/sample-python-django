from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('insert', views.insert, name='insert'),
    path('delete', views.delete, name='delete'),
    path('update_form', views.updateform),
    path('update', views.update)
]

from django.urls import path
from . import views

app_name = 'tree_menu'

urlpatterns = [
    path('', views.home, name='home'),
]

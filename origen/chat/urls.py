# chat/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sessions', views.EditSessionView, 'Sessions')

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
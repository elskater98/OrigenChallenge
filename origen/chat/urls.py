# chat/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sessions', views.EditSessionView, 'Sessions')
router.register(r'collaborate', views.EditSessionAllowedView, 'ListSessions')

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('account/register', views.UserCreate.as_view())
]
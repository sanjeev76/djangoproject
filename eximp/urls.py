from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    path('rest', include(router.urls))
]


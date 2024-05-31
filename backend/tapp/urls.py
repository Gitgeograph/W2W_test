from django.urls import path, include
from tapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tapp', TModelListAPI)

urlpatterns = [
    path('', include(router.urls))
]
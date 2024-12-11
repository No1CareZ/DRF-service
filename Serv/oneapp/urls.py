from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PrimarchViewSet, ChapterViewSet
)

router = DefaultRouter()

router.register(r'primarchs', PrimarchViewSet, basename='primarch')
router.register(r'chapters', ChapterViewSet, basename='chapters')

app_name = "oneapp"

urlpatterns = [
    path('', include(router.urls))
]

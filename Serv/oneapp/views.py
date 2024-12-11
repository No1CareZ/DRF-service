from rest_framework import viewsets

from .models import Primarch, Chapter
from .serializers import PrimarchSerializer, ChapterSerializer


class PrimarchViewSet(viewsets.ModelViewSet):
    """
    View set form Primarchs provides 'list', 'create', 'retriveve',
    'update' and 'destroy' actions.
    """
    queryset = Primarch.objects.all()
    serializer_class = PrimarchSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    """
    View set form Chapters provides 'list', 'create', 'retriveve',
    'update' and 'destroy' actions.
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

from rest_framework import generics

from backend.permissions import IsCreatorOrReadOnly
from perfumes.models import Perfume
from perfumes.serializers import PerfumeSerializer


class PerfumeListView(generics.ListCreateAPIView):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer


class PerfumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCreatorOrReadOnly]
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

from rest_framework import generics

from .models import Perfume
from .serializers import PerfumeSerializer
from backend.permissions import IsCreator


class PerfumeListView(generics.ListCreateAPIView):
    queryset = Perfume.objects.all()
    serialized_class = PerfumeSerializer


class PerfumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCreator]
    queryset = Perfume.objects.all()
    serialized_class = PerfumeSerializer

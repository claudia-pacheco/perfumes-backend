from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Perfume
from .serializers import PerfumeSerializer


class PerfumeListView(APIView):
    def get(self, _request):
        perfumes = Perfume.objects.all()
        serialized_perfumes = PerfumeSerializer(perfumes, many=True)
        return Response(serialized_perfumes.data)


class PerfumeDetailView(APIView):
    def get(self, _request, pk):
        perfume = Perfume.objects.get(id=pk)
        serialized_perfumes = PerfumeSerializer(perfume, many=False)
        return Response(serialized_perfumes.data)

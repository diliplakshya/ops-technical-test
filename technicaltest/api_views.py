from rest_framework.generics import ListAPIView
from technicaltest.serializers import HomeSerializer, MetaDataSerializer
from technicaltest.models import Home, MetaData

class HomeList(ListAPIView):
    """Root End Point"""
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class MetaDataList(ListAPIView):
    """Application Metadata"""
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer

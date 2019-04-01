"""
This module is the REST API view for Home and Meta Data request.
"""


from rest_framework.generics import ListAPIView
from technicaltest.serializers import HomeSerializer, MetaDataSerializer
from technicaltest.models import Home, MetaData


class HomeApiView(ListAPIView):
    """
    REST API view for Home View.
    """
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class MetaDataApiView(ListAPIView):
    """
    REST API view for Meta Data View.
    """
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer

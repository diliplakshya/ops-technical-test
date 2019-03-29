from rest_framework.generics import ListAPIView
from technicaltest.serializers import HomeSerializer
from technicaltest.models import Home

class HomeList(ListAPIView):
    """docstring for HomeList."""
    queryset = Home.objects.last()
    serializer_class = HomeSerializer

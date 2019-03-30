from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from technicaltest.models import Home, MetaData

class HomeSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Home
        fields = ('display_text',)
        renderer = JSONRenderer()
        renderer.render(fields)
        
class MetaDataSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MetaData
        fields = ('version', 'description', 'last_commit_sha', 'commit_message')
        renderer = JSONRenderer()
        renderer.render(fields)

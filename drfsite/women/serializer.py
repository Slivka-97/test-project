from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from women.models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = WomenModel("New Actor", "Neww Actor content")
    model_sr = WomenSerializer(model)
    print(model_sr.data)
    json = JSONRenderer().render(model_sr.data)
    print(json)

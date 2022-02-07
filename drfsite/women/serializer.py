from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from women.models import Women


#class WomenModel:
    #def __init__(self, title, content, cat_id):
        #self.title = title
        #self.content = content
        #self.cat_id = cat_id


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)




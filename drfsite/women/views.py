from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializer import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        # l = list()
        # for i in lst:
        #    l.append(i.content)
        return Response({'posts': lst})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
    # queryset = Women.objects.all()
    # serializer_class = WomenSerializer

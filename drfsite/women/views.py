from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from setuptools._distutils.command.install_data import install_data

from .models import Women
from .serializer import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDelete(generics.DestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIView(APIView):

    def get(self, request):
        lst = Women.objects.all().values()
        # l = list()
        # for i in lst:
        #    l.append(i.content)
        return Response({'posts': lst})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, pk):
        if not pk:
            return Response({'Error': 'Method PUT not allowed'})
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'Error': 'Object not exists'})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'pots': serializer.data})

    def delete(self, request, pk):
        if not pk:
            return Response({'Error': 'Method DELETE not allowed'})
        try:
            instance = Women.objects.get(pk=pk).delete()

            return Response({'delete': 'delete'})

        except:
            return Response({'Error': 'Object not exists'})

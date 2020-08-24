from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from good.models import Good
from good.serializers import GoodSerializer

class GoodFilter(generics.ListCreateAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('title', 'price', 'size')


class GoodBySubCategoryIdAPIView(APIView):

    def get(self, request, subcategory_id):
        goods = Good.objects.filter(subcategory=subcategory_id)
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)



class GoodDetailsAPIView(APIView):

    def get_object(self, good_id):
        try:
            return Good.objects.get(id=good_id)
        except Good.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, good_id):
        good = self.get_object(good_id)
        serializer = GoodSerializer(good)
        return Response(serializer.data)

    def put(self, request, good_id):
        good = self.get_object(good_id)
        serializer = GoodSerializer(instance=good, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors})

    def delete(self, request, good_id):
        good = self.get_object(good_id)
        good.delete()
        return Response({'deleted':True})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer


class VendorProductMappingListCreate(APIView):

    def get(self, request):

        data = VendorProductMapping.objects.all()
        serializer = VendorProductMappingSerializer(data, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
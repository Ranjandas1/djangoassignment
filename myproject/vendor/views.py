from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer


class VendorListCreate(APIView):

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class VendorDetail(APIView):

    def get_object(self, id):
        return Vendor.objects.get(id=id)

    def get(self, request, id):
        vendor = self.get_object(id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, id):
        vendor = self.get_object(id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        vendor = self.get_object(id)
        vendor.delete()
        return Response(status=204)
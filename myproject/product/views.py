from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer
from vendor_product_mapping.models import VendorProductMapping


class ProductListCreate(APIView):

    def get(self, request):

        vendor_id = request.query_params.get("vendor_id")

        queryset = Product.objects.all()
        if vendor_id:
            queryset = Product.objects.filter(
                id__in=VendorProductMapping.objects.filter(
                    vendor_id=vendor_id
                ).values_list("product_id", flat=True)
            )

        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductDetail(APIView):

    def get_object(self, id):

        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None


    def get(self, request, id):

        product = self.get_object(id)

        if not product:
            return Response({"error": "Product not found"}, status=404)

        serializer = ProductSerializer(product)

        return Response(serializer.data)


    def put(self, request, id):

        product = self.get_object(id)

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def patch(self, request, id):

        product = self.get_object(id)

        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        product = self.get_object(id)

        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
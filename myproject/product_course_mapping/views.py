from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer


class ProductCourseMappingListCreate(APIView):

    def get(self,request):

        data = ProductCourseMapping.objects.all()
        serializer = ProductCourseMappingSerializer(data,many=True)

        return Response(serializer.data)


    def post(self,request):

        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)

        return Response(serializer.errors,status=400)
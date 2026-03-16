from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreate(APIView):

    def get(self,request):

        data = CourseCertificationMapping.objects.all()
        serializer = CourseCertificationMappingSerializer(data,many=True)

        return Response(serializer.data)


    def post(self,request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)

        return Response(serializer.errors,status=400)
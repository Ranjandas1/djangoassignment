from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Certification
from .serializers import CertificationSerializer
from course_certification_mapping.models import CourseCertificationMapping


class CertificationListCreate(APIView):

    def get(self, request):

        course_id = request.query_params.get("course_id")

        queryset = Certification.objects.all()
        if course_id:
            queryset = Certification.objects.filter(
                id__in=CourseCertificationMapping.objects.filter(
                    course_id=course_id
                ).values_list("certification_id", flat=True)
            )

        serializer = CertificationSerializer(queryset, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = CertificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class CertificationDetail(APIView):

    def get_object(self, id):

        try:
            return Certification.objects.get(id=id)
        except Certification.DoesNotExist:
            return None


    def get(self, request, id):

        obj = self.get_object(id)

        if not obj:
            return Response({"error": "Not found"}, status=404)

        serializer = CertificationSerializer(obj)

        return Response(serializer.data)


    def put(self, request, id):

        obj = self.get_object(id)

        serializer = CertificationSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request, id):

        obj = self.get_object(id)

        obj.delete()

        return Response(status=204)
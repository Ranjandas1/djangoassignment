from rest_framework import serializers
from .models import Certification
from course.models import Course
from course_certification_mapping.models import CourseCertificationMapping


class CertificationSerializer(serializers.ModelSerializer):

    course = serializers.CharField(write_only=True)

    class Meta:
        model = Certification
        fields = [
            "course",
            "name",
            "code",
            "description",
            "is_active"
        ]


    def to_internal_value(self, data):

        course_value = data.get("course")

        if not course_value:
            raise serializers.ValidationError(
                {"course": "Course id, code, or name is required"}
            )

        course = None

        if str(course_value).isdigit():
            course = Course.objects.filter(id=course_value).first()

        if not course:
            course = Course.objects.filter(code=course_value).first()

        if not course:
            course = Course.objects.filter(name=course_value).first()

        if not course:
            raise serializers.ValidationError(
                {"course": "Course not found"}
            )

        data["course_obj"] = course

        return super().to_internal_value(data)


    def create(self, validated_data):

        course = validated_data.pop("course_obj")
        validated_data.pop("course")

        certification = Certification.objects.create(**validated_data)

        CourseCertificationMapping.objects.create(
            course=course,
            certification=certification,
            primary_mapping=True,
            is_active=True
        )

        return certification
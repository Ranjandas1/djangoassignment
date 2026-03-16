from rest_framework import serializers
from .models import Course
from product.models import Product
from product_course_mapping.models import ProductCourseMapping


class CourseSerializer(serializers.ModelSerializer):

    product = serializers.CharField(write_only=True)

    class Meta:
        model = Course
        fields = [
            "product",
            "name",
            "code",
            "description",
            "is_active"
        ]


    def to_internal_value(self, data):

        product_value = data.get("product")

        if not product_value:
            raise serializers.ValidationError(
                {"product": "Product id, code, or name is required"}
            )

        product = None

        if str(product_value).isdigit():
            product = Product.objects.filter(id=product_value).first()

        if not product:
            product = Product.objects.filter(code=product_value).first()

        if not product:
            product = Product.objects.filter(name=product_value).first()

        if not product:
            raise serializers.ValidationError(
                {"product": "Product not found"}
            )

        data["product_obj"] = product

        return super().to_internal_value(data)


    def create(self, validated_data):

        product = validated_data.pop("product_obj")
        validated_data.pop("product")

        course = Course.objects.create(**validated_data)

        ProductCourseMapping.objects.create(
            product=product,
            course=course,
            primary_mapping=True,
            is_active=True
        )

        return course
from rest_framework import serializers
from .models import Product
from vendor.models import Vendor
from vendor_product_mapping.models import VendorProductMapping


class ProductSerializer(serializers.ModelSerializer):

    vendor = serializers.CharField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "vendor",
            "name",
            "code",
            "description",
            "is_active"
        ]


    def to_internal_value(self, data):

        vendor_value = data.get("vendor")

        if not vendor_value:
            raise serializers.ValidationError(
                {"vendor": "Vendor id, code, or name is required"}
            )

        vendor = None

        if str(vendor_value).isdigit():
            vendor = Vendor.objects.filter(id=vendor_value).first()

        if not vendor:
            vendor = Vendor.objects.filter(code=vendor_value).first()

        if not vendor:
            vendor = Vendor.objects.filter(name=vendor_value).first()

        if not vendor:
            raise serializers.ValidationError(
                {"vendor": "Vendor not found"}
            )

        data["vendor_obj"] = vendor

        return super().to_internal_value(data)


    def create(self, validated_data):

        vendor = validated_data.pop("vendor_obj")
        validated_data.pop("vendor")

        product = Product.objects.create(**validated_data)

        VendorProductMapping.objects.create(
            vendor=vendor,
            product=product,
            primary_mapping=True,
            is_active=True
        )

        return product
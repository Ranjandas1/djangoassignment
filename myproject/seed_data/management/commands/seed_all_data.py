import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from vendor.models import Vendor
from product.models import Product
from course.models import Course
from certification.models import Certification

from vendor_product_mapping.models import VendorProductMapping
from product_course_mapping.models import ProductCourseMapping
from course_certification_mapping.models import CourseCertificationMapping


class Command(BaseCommand):

    help = "Load seed data from JSON files"

    def load_json(self, filename):
        path = os.path.join(settings.BASE_DIR, "seed_data/data", filename)

        with open(path) as f:
            return json.load(f)

    def handle(self, *args, **kwargs):

        vendors = self.load_json("vendors.json")

        for v in vendors:
            Vendor.objects.get_or_create(
                code=v["code"],
                defaults=v
            )

        products = self.load_json("products.json")

        for p in products:

            vendor = Vendor.objects.get(code=p["vendor_code"])

            product, _ = Product.objects.get_or_create(
                code=p["code"],
                defaults={
                    "name": p["name"],
                    "description": p["description"]
                }
            )

            VendorProductMapping.objects.get_or_create(
                vendor=vendor,
                product=product,
                defaults={
                    "primary_mapping": True,
                    "is_active": True
                }
            )

        courses = self.load_json("courses.json")

        for c in courses:

            product = Product.objects.get(code=c["product_code"])

            course, _ = Course.objects.get_or_create(
                code=c["code"],
                defaults={
                    "name": c["name"],
                    "description": c["description"]
                }
            )

            ProductCourseMapping.objects.get_or_create(
                product=product,
                course=course,
                defaults={
                    "primary_mapping": True,
                    "is_active": True
                }
            )

        certifications = self.load_json("certifications.json")

        for cert in certifications:

            course = Course.objects.get(code=cert["course_code"])

            certification, _ = Certification.objects.get_or_create(
                code=cert["code"],
                defaults={
                    "name": cert["name"],
                    "description": cert["description"]
                }
            )

            CourseCertificationMapping.objects.get_or_create(
                course=course,
                certification=certification,
                defaults={
                    "primary_mapping": True,
                    "is_active": True
                }
            )

        self.stdout.write(
            self.style.SUCCESS("All seed data loaded successfully")
        )
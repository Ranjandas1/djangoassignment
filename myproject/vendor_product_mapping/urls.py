from django.urls import path
from .views import VendorProductMappingListCreate

urlpatterns = [
    path('vendor-product-mappings/', VendorProductMappingListCreate.as_view()),
]
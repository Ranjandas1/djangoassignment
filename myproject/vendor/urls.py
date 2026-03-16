from django.urls import path
from .views import VendorListCreate, VendorDetail

urlpatterns = [
    path('vendors/', VendorListCreate.as_view()),
    path('vendors/<int:id>/', VendorDetail.as_view()),
]
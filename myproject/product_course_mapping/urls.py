from django.urls import path
from .views import ProductCourseMappingListCreate

urlpatterns = [
    path('product-course-mappings/', ProductCourseMappingListCreate.as_view()),
]
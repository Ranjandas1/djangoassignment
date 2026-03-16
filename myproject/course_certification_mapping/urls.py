from django.urls import path
from .views import CourseCertificationMappingListCreate

urlpatterns = [
    path('course-certification-mappings/', CourseCertificationMappingListCreate.as_view()),
]
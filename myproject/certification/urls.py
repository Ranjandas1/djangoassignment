from django.urls import path
from .views import CertificationListCreate, CertificationDetail

urlpatterns = [

    path('certifications/', CertificationListCreate.as_view()),
    path('certifications/<int:id>/', CertificationDetail.as_view()),

]
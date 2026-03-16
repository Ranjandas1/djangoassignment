from django.urls import path
from .views import CourseListCreate, CourseDetail

urlpatterns = [

    path('courses/', CourseListCreate.as_view()),
    path('courses/<int:id>/', CourseDetail.as_view()),

]
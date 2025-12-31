
from django.urls import path
from . import views
from .views import Student_list_create

urlpatterns = [
    path('student/',Student_list_create.as_view(),name='student_api'),
    path('student/<int:pk>/',Student_list_create.as_view(),name='student_detail_api'),
]

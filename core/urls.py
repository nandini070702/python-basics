from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('api/', views.api_home),
    path('students/create/', views.create_student),
    path('students/', views.get_students),
    path('students/<int:student_id>/update/', views.update_student),
    path('students/<int:student_id>/delete/', views.delete_student),
    path('drf/students/', views.drf_get_students),
    path('drf/students/create/', views.drf_create_student),
    path('drf/students/<int:student_id>/update/', views.drf_update_student),
    path('drf/students/<int:student_id>/delete/', views.drf_delete_student),



]

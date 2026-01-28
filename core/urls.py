from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('api/', views.api_home),
    path('students/create/', views.create_student),
    path('students/', views.get_students),


]

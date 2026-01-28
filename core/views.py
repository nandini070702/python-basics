from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.models import Student
from django.http import JsonResponse

def home(request):
    data = {
        "name": "Nandini",
        "role": "Backend Learner"
    }
    return render(request, "core/home.html", data)

def about(request):
    return HttpResponse("About page")

def api_home(request):
    return JsonResponse({
        "message": "Welcome to Django API",
        "status": "success"
    })
def create_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")

        student = Student(
            name=name,
            age=age,
            email=email
        )
        student.save()

        return JsonResponse({
            "message": "Student created successfully"
        })

    else:
        return JsonResponse({
            "error": "GET method not allowed. Use POST."
        }, status=400)

def get_students(request):
    students = Student.objects.all()

    data = []

    for student in students:
        data.append({
            "name": student.name,
            "age": student.age,
            "email": student.email
        })

    return JsonResponse({
        "students": data
    })

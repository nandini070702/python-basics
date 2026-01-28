from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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

import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"User: {username}\nPassword: {password}")
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"message": "Invalid credentials"})
    return JsonResponse({"message": "This is login view"})
        
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logout view"})

@csrf_exempt
def register_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "Username already exists"})
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({"message": "User created successfully"})
    return JsonResponse({"message": "it's user created view"})

def hello(request):
    return HttpResponse("<H1>Hello, world!</H1>")


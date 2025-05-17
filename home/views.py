import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from home.models import UserDetail

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

def index(request):
    return HttpResponse("Hello from the travel app backend!")


@csrf_exempt
def home_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        country = data.get("country")
        destination = data.get("destination")
        details = UserDetail(name=name, select_country=country, select_destination_type=destination)
        details.save()
        print(f"{name}-{country}-{destination}")
        return JsonResponse({"message": "Success"})
    return JsonResponse({"message":"This is details page"})



from django.shortcuts import render
from .import views
import json
from .models import Register
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt #security purpose
def reg(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        fname = data.get("fname")
        lname = data.get("lname")
        phone = data.get("phone")
        email = data.get("email")
        password = data.get("password")

        Register.objects.create(
            fname=fname,
            lname=lname,
            phone=phone,
            email=email,
            password=password
        )

        return JsonResponse({"message": "Registered Successfully"}, status=201)

    return JsonResponse({"error": "POST Method Only"}, status=405)

@csrf_exempt
def login(request):
    if(request.method=="POST"): #to retrieve the data from postman
        data=json.loads(request.body.decode("utf-8")) #change it to python dictionary format from string
        email=data.get("email") #to get the value of email key
        password=data.get("password") #get the value of password key

  
        user=Register.objects.get(email=email,password=password) #to check whether the email and password are correct or not
        if user:
            return JsonResponse({"message":"Login Successful"}) #if credentials are correct
        else:
            return JsonResponse({"error":"Invalid Credentials"}) #if credentials are incorrect
    return JsonResponse({"error": "POST method only"}) #if method is not post
    
@csrf_exempt
def get_data(request):
    if request.method == "GET":
        data=Register.objects.all()
        sample = []
        for i in data:
            sample.append({

            "fname":i.fname,
            "lname":i.lname,
            "phone":i.phone,
            "email":i.email,
            "password":i.password

            })
            return JsonResponse({"users":sample})
    return JsonResponse({"error":"GET method only"})    
@csrf_exempt
def get_users(request): 
    if request.method == "DELETE":
        data = json.loads(request.body.decode("utf-8")) 
        id = data.get("id")
        removed_user = Register.objects.filter(id=id)
        if removed_user.exists():
            removed_user.delete()
            return JsonResponse({"message": f"User with id {id} deleted"}, status=200)
        else:
            return JsonResponse({"error": "User not found"}, status=404)            
    return JsonResponse({"error": "DELETE method only"}, status=405)
    
@csrf_exempt
def update_user(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        id = data.get("id")
        if not Register.objects.filter(id=id).exists():
            return JsonResponse({"error": "User not found"}, status=404)
        Register.objects.filter(id=id).update(
        fname = data.get("fname"),
        lname = data.get("lname"),
        phone = data.get("phone"),
        email = data.get("email"),
        password = data.get("password")
        )
        
        return JsonResponse({"message": "User updated successfully"}, status=200)

    return JsonResponse({"error": "PUT method only"}, status=405)
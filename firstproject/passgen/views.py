from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    password = ""

    for x in range(15): # Generate a 10-character password
        password += random.choice(characters) # Add a random character to the password
    
    result = {'password': password}

    return JsonResponse(result)

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return render(request,'home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('digits'):
        characters.extend(list('0123456789'))

    if request.GET.get('symbols'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 10))

    password = ""

    for x in range(length): # Loop through the length of the password
        password += random.choice(characters) # Add a random character to the password

    return render(request, 'password.html', {'password': password})

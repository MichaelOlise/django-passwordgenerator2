from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator2/home.html')

def about(request):
    return render(request, 'generator2/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    lenght = int(request.GET.get('lenght',12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request,'generator2/password.html', {'password':thepassword})

from string import ascii_lowercase, ascii_uppercase
from random import choice

from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    character = list(ascii_lowercase)

    if request.GET.get('uppercase'):
        character.extend(list(ascii_uppercase))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        character.extend(list('1234567890'))

    length = request.GET.get('length')
    gen_password = ''
    for i in range(int(length)):
        gen_password += choice(character)

    return render(request, 'generator/password.html', {'password': gen_password})

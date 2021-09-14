from string import ascii_lowercase
from string import ascii_uppercase
from random import choice

from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    charaters = list(ascii_lowercase)

    if request.GET.get('uppercase'):
        charaters.extend(list(ascii_uppercase))
    if request.GET.get('special'):
        charaters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        charaters.extend(list('1234567890'))

    length = request.GET.get('length')
    gen_password = ''
    for i in range(int(length)):
        gen_password += choice(charaters)

    return render(request, 'generator/password.html', {'password': gen_password})

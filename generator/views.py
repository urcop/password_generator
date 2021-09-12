from django.shortcuts import render
from string import ascii_letters
from random import choice


def home(request):
    letters = ascii_letters
    password = ''
    for i in range(1, 10):
        password += choice(letters)

    return render(request, 'generator/home.html', {'password': password})

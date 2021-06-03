from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}, você tem  {idade} anos</h1>')


def soma(request, a, b):
    return HttpResponse(f'Soma de {a} + {b} = {a + b}')


def multiplicacao(request, a, b):
    return HttpResponse(f'Soma de {a} * {b} = {a * b}')


def divisao(request, a, b):
    return HttpResponse(f'Soma de {a} / {b} = {a / b}')


def subtracao(request, a, b):
    return HttpResponse(f'Soma de {a} - {b} = {a - b}')

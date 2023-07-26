from django.shortcuts import render
from django.http import HttpResponse

def feedback(request):
    s = [1, 2, 3, 4, 5, 6]
    one = [x ** 2 for x in s]
    print(one)
    return HttpResponse(f'Квадраты чисел от 1 до 6 это {one}')
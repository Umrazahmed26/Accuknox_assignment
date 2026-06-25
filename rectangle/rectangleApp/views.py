from django.shortcuts import render

from django.http import JsonResponse
from .rectangle import Rectangle


def test_rectangle(request):

    rect = Rectangle(10, 5)

    result = []

    for item in rect:
        result.append(item)

    return JsonResponse(result, safe=False)
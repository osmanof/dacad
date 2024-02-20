import json

from django.http import HttpResponse
from django.shortcuts import render


def answer(request):
    return HttpResponse(json.dumps([
        ["1.", "Ильясов Ахмад", "ah@mad.ru", 52, 56.7],
        ["2.", "2Ильясов Ахмад", "ah@mad.ru", 8, 56.7],
        ["3.", "1Ильясов Рустамохаир", "ah@mad.ru", 50, 56.7]
    ]))


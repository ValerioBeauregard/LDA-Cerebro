import json

import openai

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import User, Niveles


def index(request):
  data = Niveles.objects.all()
  return render(request, "smartwater/index.html", {'data': data})

@csrf_exempt
def nivel_save(request):
  if request.method == "POST":
    # Getting current user
    current_user = request.user

    # Getting request data
    data = json.loads(request.body)

    id_dispositivo = data.get("id_dispositivo")
    nivel = data.get("nivel")
    motor = data.get("motor")
    fuente = data.get("fuente")

    # Getting the company
    registro = Niveles.objects.create(id_dispositivo=id_dispositivo, nivel=nivel, motor=motor, fuente=fuente)

    # Applying changes
    registro.save()

    return JsonResponse({"Success": 'Data saved successfully!'}, safe=False)




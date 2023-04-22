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

SECRET_KEY = "JHo927j-LDA_220423/?d?v?=2-23jgh"

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

    secret_key = data.get("secret_key")
    id_dispositivo = data.get("id_dispositivo")
    nivel = data.get("nivel")
    motor = data.get("motor")
    fuente = data.get("fuente")

    if secret_key == SECRET_KEY:
      # Making the register
      registro = Niveles.objects.create(id_dispositivo=id_dispositivo, nivel=nivel, motor=motor, fuente=fuente)

      # Applying changes
      registro.save()

      return JsonResponse({"Success": 'Data saved successfully!'}, status=200, safe=False)

    else:
      return JsonResponse({"error": 'You are not authorized'}, status=401, safe=False)





import json
import os
from django.shortcuts import redirect
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def application(request):
    return render(request, 'application.html')

def rejoindre(request):
    return render(request, 'rejoindre.html')

def waitlist(request):
    if request.method == 'POST':
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')

        donnees = {
            'telephone': telephone,
            'email': email,
        }

        fichier = os.path.join(settings.BASE_DIR, 'formulaire.json')

        if os.path.exists(fichier):
            with open(fichier, 'r') as f:
                donnees_existantes = json.load(f)
                donnees_existantes.append(donnees)
            with open(fichier, 'w') as f:
                json.dump(donnees_existantes, f)
        else:
            with open(fichier, 'w') as f:
                json.dump([donnees], f)
        messages.success(request, 'Votre action a été effectuée avec succès !')
        return redirect('/application')
    messages.error(request, 'Une erreur est survenue.')
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
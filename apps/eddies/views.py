from django.shortcuts import render
#from apps.eddies.models import MODEL


def eddies(request):
    return render(request, "eddies/eddies.html", {},)

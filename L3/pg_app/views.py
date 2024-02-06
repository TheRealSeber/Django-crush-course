from django.shortcuts import render
from . import models


# Create your views here.
def list_patients(request):
    patients = models.Patient.objects.all()
    context = {"patients": patients}

    return render(request, "pg_app/list_patients.html", context)

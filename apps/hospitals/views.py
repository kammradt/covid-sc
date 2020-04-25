from django.shortcuts import render

from apps.hospitals.models import Hospital


def index(request):
    return render(request, 'index.html', {})


def hospital_general_data(request, hospital_id):
    hospital = Hospital.objects.get(pk=hospital_id)

    return render(request, 'hospital/general_data.html', {
        'hospital': hospital
    })

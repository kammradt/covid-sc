from django.shortcuts import render

from apps.hospitals.models import Hospital, Report


def index(request):
    return render(request, 'index.html', {})


def show(request, hospital_id):
    hospital = Hospital.objects.get(pk=hospital_id)
    report = Report.objects.filter(hospital=hospital_id).order_by('-report_date').first()

    return render(request, 'hospital/show.html', {
        'hospital': hospital,
        'report': report
    })

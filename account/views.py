from django.shortcuts import render
from django.http import HttpResponse


def dashboard(request):
    ru = "Привет"
    return render(request, 'dashboard.html', {'section': ru})

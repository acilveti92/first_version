# Create your views here.
from datetime import datetime

from django.shortcuts import render

# Imports must either be relative, like this, or have the full path
from .models import Line


def home(request):
    return render(request, 'home.html', {'right_now':datetime.utcnow(), "lines" : Line.objects.all()})
# Create your views here.
from datetime import datetime

from django.shortcuts import render

from rest_framework import serializers, viewsets

# Imports must either be relative, like this, or have the full path
from .models import Line


def home(request):
    return render(request, 'home.html', {'right_now':datetime.utcnow(), "lines" : Line.objects.all()})


# Serializers define the API representation.
class LineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        exclude = []


# ViewSets define the view behavior.
class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

# Create your views here.
from datetime import datetime

from django.shortcuts import render

from rest_framework import serializers, viewsets

from django.http import HttpResponse

# Imports must either be relative, like this, or have the full path
from .models import Line, Word


def home(request):
    return render(request, 'home.html', {'right_now':datetime.utcnow(), "lines" : Line.objects.all()})


def hello(request):
    return HttpResponse('Hello World!')


# Serializers define the API representation.
class LineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        exclude = []


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        exclude = []


# ViewSets define the view behavior.
class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_fields = ['english_text', 'spanish_text']

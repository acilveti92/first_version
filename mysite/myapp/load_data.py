from datetime import datetime



#from django.shortcuts import render

from rest_framework import serializers, viewsets, request, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
from django.template import RequestContext, Template
from django.shortcuts import render, redirect, get_object_or_404  #from tutorial  Beginner
from django.contrib.auth import authenticate, login  #from tutorial  Beginner
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View  #from tutorial  Beginner
from .forms import UserForm  #from tutorial  Beginner

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

import ebooklib
from ebooklib import epub


# Imports must either be relative, like this, or have the full path
from .models import Line, Word, WordsUse, WordAjaxModel
from .serializers import WordSerializer, WordAjaxSerializer

from bs4 import BeautifulSoup   #for html handling
from bs4 import NavigableString

import re

import urllib.request

from models import PruebaExcel

import csv


# Full path and name to your csv file
csv_filepathname="/home/acilveti92/mysite/mysite/myapp/pruebaexcel.csv"
# Full path to your django project directory
your_djangoproject_home="/home/acilveti92/mysite/mysite/myapp/"


with open(csv_filepathname) as f:
        reader = csv.reader(f)
        for row in reader:
            PruebaExcel.name = row[0]
            PruebaExcel.number = row[1]
            PruebaExcel.save()

            # creates a tuple of the new object or
            # current object and a boolean of if it was created



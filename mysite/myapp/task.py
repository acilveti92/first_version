from celery import task
# Create your views here.
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
from .models import Line, Word, WordsUse, WordAjaxModel, PruebaExcel
from .serializers import WordSerializer, WordAjaxSerializer

from bs4 import BeautifulSoup   #for html handling
from bs4 import NavigableString

import re

import urllib.request



import csv

from collections import Counter



@task()
def celerytest(x, y):
    print("this is celery test")


    return x + y
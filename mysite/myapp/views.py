# Create your views here.
from datetime import datetime



#from django.shortcuts import render

from rest_framework import serializers, viewsets, request, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404  #from tutorial  Beginner
from django.contrib.auth import authenticate, login  #from tutorial  Beginner
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View  #from tutorial  Beginner
from .forms import UserForm  #from tutorial  Beginner

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


# Imports must either be relative, like this, or have the full path
from .models import Line, Word, WordsUse
from .serializers import WordSerializer


def home(request):
    return render(request, 'home.html', {'right_now':datetime.utcnow(), "lines" : Line.objects.all()})


def hello(request):
    return HttpResponse('Hello World!')


# Serializers define the API representation.
class LineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        exclude = []

#DESCOMENTARLO
#class WordSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Word
#        exclude = []


# ViewSets define the view behavior.
class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_fields = ['english_text', 'spanish_text']

#user creation
class UserFormView(View):
    form_class =UserForm
    template_name ='registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('http://acilveti92.pythonanywhere.com/')

            return render(request,self.template_name,{'form':form})


class wordajax(APIView):
#IT ONLY WORKS WITH GET, WITH POST 403 ERROR
    def get(self, request):

        datos= request.query_params
        datos=datos.copy()
        print("the word is")
        print(datos['palabra'])
        words = Word.objects.get(english_text=datos['palabra'])
        print("the object words is ")
        print( words)
        serializer = WordSerializer(words)

        session_key = request.session._session_key
        print("the session key is")
        print(request.session._session_key)

        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        click_user = User.objects.get(pk=uid)
        print("the user is")
        print(click_user)
        word_data = WordsUse(user = click_user, english_text = words, translation_active = True, aparitions = 0, click = 0) #increment of clicked, and switch translatio_active on ((user=click_user, english_text=words, translation_active = True,

        #pruebaword = WordsUse.objects.get(aparitions=0)

        #pruebaword.user= click_user
        #pruebaword.english_text= words
        #pruebaword.translation_active=True
        #pruebaword.aparitions=0
        #pruebaword.click=0

        #task to do:
        #if-else statement for avoid repeatin word_data
        #clean the code
        #increment the click record
        #switch of the translation
        #in javascript change tehe code in the replace part.




        print("the word_data object is")
        print(word_data)
        word_data.save()



        #word_data.clicked += 1
        #word_data.save()
        #print("the word_data object is")
        #print(word_data)
        #print("fin")

        return Response(serializer.data)


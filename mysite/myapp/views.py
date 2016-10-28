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

import ebooklib
from ebooklib import epub


# Imports must either be relative, like this, or have the full path
from .models import Line, Word, WordsUse
from .serializers import WordSerializer


def home(request):
    return render(request, 'home.html', {'right_now':datetime.utcnow(), "lines" : Line.objects.all()})


def example(request):
    return render(request, 'index.html')


def hello(request):

    book = epub.read_epub('mysite/mysite/myapp/test.epub')
    print('THE BOOK IS THIS!!!!')
    print(book)
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
        word_data = WordsUse.objects.filter(user = click_user, english_text = words)
        if len(word_data) is 1:
            print("the get has returned the next object")
            print(word_data[0])
            word_data=word_data[0]
            word_data.translation_active = True
            word_data.click += 1
        else:
            if len(word_data) is 0:
                word_data = WordsUse(user = click_user, english_text = words, translation_active = True, aparitions = 0, click = 1) #increment of clicked, and switch translatio_active on ((user=click_user, english_text=words, translation_active = True,
            else:
                print(" ERROR:there are more than one DB objects." + len(word_data))


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

def newpagewords(request):
    test = "I want"
    test=test.lower()
    words = test.split()

    print(words)
    for i in range(0,len(words)):
        print(words[i])


    session_key = request.session._session_key
    print("the session key is")
    print(request.session._session_key)

    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    click_user = User.objects.get(pk=uid)
    print("the user is")
    print(click_user)

    for i in range(0,len(words)):

        words_obj = Word.objects.get(english_text = words[i])
        word_data = WordsUse.objects.filter(user = click_user, english_text = words_obj)

        if len(word_data) is 1:
            word_data_obj=word_data[0]
            print("the get has returned the next object")
            print(word_data_obj)
            word_data_obj.aparitions += 1
            word_data_obj.save()
        else:
            if len(word_data) is 0:
                print(" there was not word in DB")
                word_data = WordsUse(user = click_user, english_text = words, translation_active = True, aparitions = 1, click = 0) #increment of clicked, and switch translatio_active on ((user=click_user, english_text=words, translation_active = True,
                word_data.save()
            else:
                print(" ERROR:there are more than one DB objects." + len(word_data))

        # when certain number of aparitions are done, the translation should be switched off. task to do in the future



    print(words)
    return HttpResponse("I want")




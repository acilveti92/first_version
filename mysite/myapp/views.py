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

from mysite.myapp.task import celerytest



def home(request):




  #  loadwords(request)  #calling a function

    soup = BeautifulSoup(open('/home/acilveti92/mysite/mysite/myapp/templates/home.html'))

    print(soup.prettify())

    print("empieza el texto")
    print(soup.get_text())
    text = soup.get_text()
    print("acaba el texto")

    splittext=text.split()
    print(splittext)


    session_key = request.session._session_key
    print("the session key is")
    print(request.session._session_key)

    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    click_user = User.objects.get(pk=uid)
    print("the user is")
    print(click_user)


    print(len(splittext))
    print("here comes the boom")
    print(splittext[0])
#now there should be made a duplicate avoider algorithm to make faster the replacement

    #first filter non alfanumeric letters
    simpletext=set(splittext)   #deletes duplicates items
    print("comparation")
    print(len(splittext))
    print(len(simpletext))
    print(splittext)
    print(simpletext)

    # Remove all strings that contain non-alphanumeric characters
    # \w means a word character (i.e. alphanumeric or underscore)
    # | means or
    # $ means end of string
    word_matcher = re.compile("(?=.*\w)^(\w|'|-)+$")

    unique_words = []
    for word in simpletext:
        # Check if word contains non-alphanumeric characters
        matches = word_matcher.match(word)
        if matches:
            unique_words.append(word)

    print("--------- únique words ---------")
    print(unique_words)

    soupstring = soup.string
    print("print soupstring")
    print(soupstring)

    for tag in soup.find_all(string=re.compile(r"\b%s\b" % "want")):
        print("this is the first tag with want")
        print(tag)
        fixed_text = tag.replace('want', 'I make it!')
        fixed_string = NavigableString(fixed_text)
        new_tag = soup.new_tag("b")
        new_tag.string = tag

        print(type(fixed_string))
        print(type(tag))
        print("this is the fixed text")
        print(fixed_string)
        print(type(tag.parent))
        print(tag.parent)
        tag2=tag.parent




        tag2.string.replace_with(fixed_string)
        print("now it has changed to that")
        print(tag2.string)

    for i in range(0,len(splittext)):
        print(splittext[i])
        print(i)
        #a auxiliary list should be made in order to delete duplications
        print("tick")
        words = Word.objects.filter(english_text=splittext[i])  #there should be something to avoid the error because of the lack of word
        if len(words) is 0:
            #if it is really a word, add to the database and translate it
            print(words)
            print("tock")
        else:
            print(words)
            word_data = WordsUse.objects.filter(user = click_user, english_text = words)
            print("word_data")
            print("tock")
            if len(word_data) is 1:
                # there should be a function to count every apparition of the word, instead of doing one by one
                print("the get has returned the next object")
                print(word_data[0])

                word_data=word_data[0]
                word_data.translation_active = True
                word_data.aparitions += 1

                word_data.save()
                editor = re.sub(r"\b%s\b" % "want" , "traduccion","prueba con want")
                print("el tipo de soup es")
                print(type(soup))
                print(editor)


            else:
                if len(word_data) is 0:
                    word_data = WordsUse(user = click_user, english_text = splittext[i], translation_active = True, aparitions = 1, click = 0) #increment of clicked, and switch translatio_active on ((user=click_user, english_text=words, translation_active = True,
                else:
                    print(" ERROR:there are more than one DB objects." + len(word_data))


    souphtml=soup.prettify()

    template = Template(souphtml)
    context = RequestContext(
        request,
        {'right_now':datetime.utcnow(), "lines" : Line.objects.all()}
        )
    return HttpResponse(template.render(context))



def example(request):
    url="https://es.wikipedia.org/wiki/Parten%C3%B3n"

    req = urllib.request.Request(url)
    print("check ")
    response = urllib.request.urlopen(req)
    print("check ")
    the_page = response.read()


    #webread=urlopen('/acilveti92.pythonanywhere.com/hello/')
    print("problem ")

    soup = BeautifulSoup(the_page)

    texts = soup.get_text()
    text = soup.get_text()
    splittext=texts.split()
    simpletext=set(splittext)   #deletes after seeing words reduction
    print("comparation")
    print(len(splittext))
    print(len(simpletext))

    print("extract now")

    for elem in soup.find_all(['script', 'style']):
        elem.extract()

    print("empieza el texto")

    texts = soup.get_text()
    print("acaba el texto")

    splittext=texts.split()

    session_key = request.session._session_key
    #print("the session key is")
    #print(request.session._session_key)

    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    click_user = User.objects.get(pk=uid)
    #print("the user is")
    #print(click_user)

    print(len(splittext))
    print("here comes the boom")
    print(splittext[0])
#now there should be made a duplicate avoider algorithm to make faster the replacement

    #first filter non alfanumeric letters
    simpletext=set(splittext)   #deletes duplicates items
    print("comparation")
    print(len(splittext))
    print(len(simpletext))
    WordNumber=len(simpletext)

    return HttpResponse(text)

def example2(request):
    return render(request, 'index2.html')


def hello(request):
    Word.objects.all().delete()
    # Full path and name to your csv file
    csv_filepathname="/home/acilveti92/mysite/mysite/myapp/ingles1000csv.csv"
    # Full path to your django project directory
    your_djangoproject_home="/home/acilveti92/mysite/mysite/myapp/"


    with open(csv_filepathname, encoding = "ISO-8859-1") as f:
        reader = csv.reader(f)
        for row in reader:
            pruebaexcel = Word(english_text = row[1], spanish_text = row[0])
            #pruebaexcel=pruebaexcel[0]
            #pruebaexcel.name = row[0]
            #pruebaexcel.number = row[1]
            pruebaexcel.save()
            print(" pruebaexcel")
            print(pruebaexcel)

            # creates a tuple of the new object or
            # current object and a boolean of if it was created

    return render(request, 'home.html', {'right_now':datetime.utcnow(), "lines" : Line.objects.all()})


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

        WordAjaxModel.objects.all().delete() #initialize model
        datos= request.query_params
        datos=datos.copy()

        print("datos")
        print(datos)

        print(datos['wordsback'])

        url = datos['urlsend']


        print("buscaraqui")
        print(url)

        #celerytest.delay(2,2)



        req = urllib.request.Request(url)
        print("check ")
        response = urllib.request.urlopen(req)  # there are some problems and there should be fixed in the future
        print("check ")
        the_page = response.read()


        #webread=urlopen('/acilveti92.pythonanywhere.com/hello/')
        print("problem ")

        soup = BeautifulSoup(the_page)

        print("extract now")

        for elem in soup.find_all(['style', 'script', '[document]', 'head', 'title']):
            elem.extract()


        print("empieza el texto")

        texts = soup.get_text()
        print("acaba el texto")




        splittext=texts.split()



        session_key = request.session._session_key
        print("the session key is")
        #print(request.session._session_key)

        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        click_user = User.objects.get(pk=uid)
        print("the user is")
        #print(click_user)

        print(len(splittext))
        print("here comes the boom")
        print(splittext[0])
#now there should be made a duplicate avoider algorithm to make faster the replacement

    #first filter non alfanumeric letters
        simpletext=set(splittext)   #deletes duplicates items .REPLACE with counter
        print("comparation")
        print(len(splittext))
        print(len(simpletext))
        WordNumber=len(simpletext)


    # Remove all strings that contain non-alphanumeric characters
    # \w means a word character (i.e. alphanumeric or underscore)
    # | means or
    # $ means end of string
        word_matcher = re.compile("(?=.*\w)^(\w|'|-)+$")

        unique_words = []
        for word in simpletext:
        # Check if word contains non-alphanumeric characters
            matches = word_matcher.match(word)
            if matches:
                unique_words.append(word)

        print("--------- únique words ---------")
        print(unique_words)

        soupstring = soup.string
        #print("print soupstring")
        #print(soupstring)

        WordCount = Counter(splittext) #to count apparitions in the web
        print("collections.Counter(simpletext)")
        print(WordCount)

        WordCountOrder=WordCount.most_common(WordNumber)
        print("WordCountOrderWordCount")
        print(WordCountOrder)

        print(WordCountOrder)








        n=7 #number of word translation to be done. in the future it should be a flexible number
        TranslationArray=["z","z","z","z","z"]
        PositionArray=0 #position of TranslationArray
        TranslatedWordsNumber = 0



#first part of algorith, returning words


        if(datos['wordsback'] == "true"):
            for i in range(0,len(WordCountOrder)):   # the word translation should be create
                words = Word.objects.filter(spanish_text__iexact= WordCountOrder[i][0])  #there should be something to avoid the error because of the lack of word
                print(WordCountOrder[i][0])
                print(words)
                print(i)

                if len(words) is 1:
                    print("if len(words) is 1:")
                    print(words)


                    word_data = WordsUse.objects.filter(user = click_user, english_text = words)
                    if len(word_data) is 1:
                        print("len(word_data) is 1:")
                        print(words)
                        word_data=word_data[0]
                        print("check")

                        if n > 0:  # to control number of words. problem, need to fix
                            repeat = True
                            if word_data.translation_active is True:
                                repeat = False

                                for j in range(0,4):

                                    if WordCountOrder[i][0] == TranslationArray[j]: # only to send different word, and not the same more than once. dont use is to compare strings
                                        repeat = True

                            if repeat is False:

                                TranslationArray[PositionArray]=WordCountOrder[i][0]
                                PositionArray=PositionArray + 1
                                print("metida en translationarray")
                                print(TranslationArray)


                                #aparitions=translation frequency. For the mother language-> foreign language mode

                                word_data.translation_launch = word_data.translation_launch + 1
                                n=n-1
                                word_data.save()
                                print("word_data in traslation array")
                                print(word_data)
                                TranslatedWordsNumber += WordCountOrder[i][1]
                                TranslatedWordsPercentage = TranslatedWordsNumber/len(splittext)
                                print("TranslatedWordsNumber")
                                print(TranslatedWordsNumber)
                                print("TranslatedWordsPercentage")
                                print(TranslatedWordsPercentage)

                                if TranslatedWordsPercentage > 0.05:
                                    PositionArray = 5   # launch te response
                                    print("launch!")

                                if word_data.translation_launch > 10:  # when it has been showed more than 10 times, the translation will switch off to pass to other words. Reactivate with a click
                                    word_data.translation_active = False
                                    print(word_data)
                                    print("translation_active False")
                                    word_data.save()

                                if PositionArray is 5:
                                    print("translation array completed")
                                    #launch the response
                                    for l in range(0, PositionArray):
                                        words = Word.objects.filter(spanish_text__iexact=TranslationArray[l])  #case insesitive search
                                        print("translationarray object")
                                        print(words)
                                        print(len(words))
                                        if len(words) is 1:
                                            WordAjaxObject=WordAjaxModel(english_text = words[0].english_text, spanish_text=words[0].spanish_text)
                                            WordAjaxObject.save()


                                        #save the data with word_data.save?????


                                    #WordAjaxObject = WordAjax.objects.create(wordRef=words)
                                    WordAjaxClass=WordAjaxModel.objects.all()

                                    print("check3")
                                    #print(WordAjaxClass)
                                    #WordAjaxObject.save(force_insert=True)
                                    words = Word
                                    print("the object  WordAjaxobject is ")
                                    print( WordAjaxClass)

                                    serializer = WordSerializer(simpletext)



                                    serializer = WordAjaxSerializer(WordAjaxClass, many=True)


                                    print("now comes de serializer")
                                    print(serializer)


                                    #serializer = WordSerializer(simpletext)
                                    print("now comes the response of the first part of the algorithm")

                                    #return HttpResponse("I want")
                                    return Response(serializer.data)
                    else:   # there is a word translation, but not a especific word use for the user

                        if len(word_data) is 0:


                            #it crashes, because
                            word_data = WordsUse(user = click_user, english_text = words[0], translation_active = True, aparitions = 1, click = 0) #increment of clicked, and switch translatio_active on ((user=click_user, english_text=words, translation_active = True,
                            word_data.save()
                    word_data.save()

            print("translation array")
            print(TranslationArray)





#second part of algorithm, updatind db
        for i in range(0,len(WordCountOrder)):   # the word translation should be create
            print("new word")
            print(WordCountOrder[i][0])
            #print(i)
        #a auxiliary list should be made in order to delete duplications
            #print("tick")
            words = Word.objects.filter(spanish_text__iexact= WordCountOrder[i][0])  #there should be something to avoid the error because of the lack of word
            print("check")
            if len(words) is 0:
            #if it is really a word, add to the database and translate it
                print("if len(words) is 0:")


                pass
            else:   # there are some operations concerning the correct existence of the word
                word_data = WordsUse.objects.filter(user = click_user, english_text = words)
                print("check2")
                if len(word_data) is 1:
                    print("check3")
                # there should be a function to count every apparition of the word, instead of doing one by one
                    word_data=word_data[0]
                    #word_data.translation_active = True
                    word_data.aparitions += WordCountOrder[i][1]
                    word_data.save()






                    #print("db update")
                    #print(words[0])


                else:   # there is a word translation, but not a especific word use for the user
                    print("check4")
                    print(len(word_data))
                    if len(word_data) is 0:

                        print("db creation")
                        print(words[0])
                        #it crashes, because
                        word_data = WordsUse(user = click_user, english_text = words[0], translation_active = True, aparitions = 1, click = 0) #increment of clicked, and switch translatio_active on ((user=click_user, english_text=words, translation_active = True,
                        word_data.save()


                    else: # there are more than one db objects

                        print(" ERROR:there are more than one DB objects." )
                        print(len(word_data))





        print("translation array")
        print(TranslationArray)




        #return HttpResponse("I want")
        return HttpResponse("updated completed")

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
    print("this is a test-1")
    return HttpResponse("I want")

class loadwords(APIView):
#IT ONLY WORKS WITH GET, WITH POST 403 ERROR
    def get(self, request):
        return HttpResponse("I want")








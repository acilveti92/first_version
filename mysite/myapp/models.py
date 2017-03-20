# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Line(models.Model):                    # model - class    - table
    text = models.CharField(max_length=255)  # field   - column


# Store translations - is ASCII enough?
class Word(models.Model):                    # model - class    - table
    english_text = models.CharField(max_length=255)
    spanish_text = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.english_text, self.spanish_text)


class WordAjaxModel(models.Model):                    # model - class    - table
    english_text = models.CharField(max_length=255)
    spanish_text = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.english_text, self.spanish_text)

class WordAjaxModelStatus(models.Model):                    # model - class    - table
    english_text = models.CharField(max_length=255)
    spanish_text = models.CharField(max_length=255)
    words_status = models.CharField(max_length=2)


    def __str__(self):
        return '%s - %s - %s' % (self.english_text, self.spanish_text, self.words_status)




class WordsUse(models.Model):                    # model - class    - table
    user = models.ForeignKey(User, null=True)
    english_text = models.ForeignKey(Word, null=True)
    translation_active = models.BooleanField(default=False)
    aparitions = models.IntegerField(default=0)
    click = models.IntegerField(default=0)
    translation_launch = models.IntegerField(default=0)


    UNKNOWN = 'UN'
    STARTED = 'ST'
    LIGHTKNOWN = 'LK'
    HEAVYKNOWN = 'HK'
    STATE_WORD_LEARNING = (
        (UNKNOWN, 'Unknown'),
        (STARTED, 'Started'),
        (LIGHTKNOWN, 'Lightknown'),
        (HEAVYKNOWN, 'Heavyknown'),
        )

    word_status = models.CharField(max_length=2, choices=STATE_WORD_LEARNING, default = 'UN')




    def __str__(self):
        return '%s - %s- %s- %s- %s- %s- %s' % ( self.user, self.english_text, self.word_status, self.translation_active, self.aparitions, self.click, self.translation_launch)


class PruebaExcel(models.Model):                    # model - class    - table
    name = models.CharField(max_length=255)
    number = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.name, self.number)

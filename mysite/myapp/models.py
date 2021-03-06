# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Line(models.Model):                    # model - class    - table
    text = models.CharField(max_length=255)  # field   - column


# Store translations - is ASCII enough?
class Word(models.Model):                    # model - class    - table
    english_text = models.CharField(max_length=255)
    spanish_text = models.CharField(max_length=255)
    translation = models.CharField(max_length=255, default="EN-GE")

    def __unicode__(self):
        return u'%s- %s - %s' % (self.english_text, self.spanish_text, self.translation)


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


class UserLanguage(models.Model):                    # model - class    - table
    user = models.ForeignKey(User, null=True)
    translation = models.CharField(max_length=6, default="EN-GE")
    translation_launch_hk = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.user, self.translation)

class UserLanguage2(models.Model):                    # model - class    - table
    user = models.ForeignKey(User, null=True)
    translation = models.CharField(max_length=6, default="EN-GE")
    translation_launch_hk = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.user, self.translation)

class UserRegister(models.Model):                    # model - class    - table
    user = models.ForeignKey(User, null=True)




    def __str__(self):
        return '%s' % (self.user)




class WordsUse(models.Model):                    # model - class    - table
    user = models.ForeignKey(User, null=True)
    english_text = models.ForeignKey(Word, null=True)
    translation_active = models.BooleanField(default=False)
    aparitions = models.IntegerField(default=0)
    click = models.IntegerField(default=0)
    translation_launch_st = models.IntegerField(default=0)
    translation_launch_lk = models.IntegerField(default=0)
    translation_launch_hk = models.IntegerField(default=0)
    aparitions_hk = models.IntegerField(default=0)


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

    #created = models.DateTimeField(editable=False)
    #modified = models.DateTimeField()

    #def save(self, *args, **kwargs):
    #    ''' On save, update timestamps '''
    #    if not self.id:
    #        self.created = timezone.now()
    #    self.modified = timezone.now()
    #    return super(User, self).save(*args, **kwargs)




    def __unicode__(self):
        return u'%s - %s- %s- %s- %s- %s- %s- %s- %s- %s' % ( self.user, self.english_text, self.word_status, self.translation_active, self.aparitions, self.click, self.translation_launch_st, self.translation_launch_lk, self.translation_launch_hk, self.aparitions_hk)


class PruebaExcel(models.Model):                    # model - class    - table
    name = models.CharField(max_length=255)
    number = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.name, self.number)


#model upload file
class Document(models.Model):
    user = models.ForeignKey(User, null=True)
    description = models.CharField(max_length=255, blank=True)
    description2 = models.CharField(max_length=255, blank=True)

    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' % (self.user, self.description, self.uploaded_at)

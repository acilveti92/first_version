from django.db import models

# Create your models here.

class Line(models.Model):                    # model - class    - table
    text = models.CharField(max_length=255)  # field   - column


# Store translations - is ASCII enough?
class Word(models.Model):                    # model - class    - table
    english_text = models.CharField(max_length=255)
    spanish_text = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.english_text, self.spanish_text)

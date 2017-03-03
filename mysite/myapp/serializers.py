from rest_framework import serializers
from .models import Word, WordAjaxModel

class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ('spanish_text','english_text',)

class WordAjaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordAjaxModel
        fields = ('english_text', 'spanish_text',)

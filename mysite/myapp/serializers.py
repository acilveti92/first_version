from rest_framework import serializers
from .models import Word, WordAjax

class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ('spanish_text',)

class WordAjaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordAjax
        fields = ('english_text', 'spanish_text',)

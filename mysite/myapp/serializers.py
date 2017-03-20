from rest_framework import serializers
from .models import Word, WordAjaxModel, WordAjaxModelStatus

class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ('spanish_text','english_text',)

class WordAjaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordAjaxModel
        fields = ('english_text', 'spanish_text',)

class WordAjaxModelStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordAjaxModelStatus
        fields = ('english_text', 'spanish_text', 'words_status',)


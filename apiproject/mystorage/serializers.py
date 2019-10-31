#django 의 form과 유사한 역할을 한다
from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')

class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source = 'author.username')
    image = serializers.ImageField(use_url = True) #image가 잘 올라갔는지 확인하겠당

    class Meta: 
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')



class FileSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = Files
        fields = ('pk', 'author_name', 'myfile', 'desc')

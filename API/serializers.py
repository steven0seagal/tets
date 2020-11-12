from rest_framework import serializers
from .models import MovieData,Comment,Rating


class MovieDataSerializer(serializers.Serializer):

    # id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=512)
    year = serializers.IntegerField()
    rated = serializers.CharField(max_length=512)
    released = serializers.CharField(max_length=512)
    runtime = serializers.CharField(max_length=512)
    genre = serializers.CharField(max_length=512)
    director = serializers.CharField(max_length=512)
    writer = serializers.CharField(max_length=512)
    actors = serializers.CharField(max_length=512)
    plot = serializers.CharField(max_length=1024)
    language = serializers.CharField(max_length=512)
    country = serializers.CharField(max_length=512)
    awards = serializers.CharField(max_length=512)
    poster = serializers.CharField(max_length=512)
    metascore = serializers.CharField(max_length=512)
    imdbrating = serializers.CharField(max_length=512)
    imdbvotes = serializers.CharField(max_length=512)
    imdbid = serializers.CharField(max_length=512)
    type = serializers.CharField(max_length=512)
    dvd= serializers.CharField(max_length=512) 
    boxoffice = serializers.CharField(max_length=512)
    production = serializers.CharField(max_length=512)
    website = serializers.CharField(max_length=512)
    response= serializers.CharField(max_length=512)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        return MovieData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        
        instance.save()
        return instance

class MovieDetailCommentSerializer(serializers.Serializer):

    comment = serializers.CharField(max_length=128)
    movie = MovieDataSerializer()
    # movie = serializers.ForeignKeyField(MovieDataSerializer, on_delete=models.CASCADE, to_field='id', db_column='title')


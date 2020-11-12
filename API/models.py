from django.db import models

# Create your models here.

class MovieData(models.Model):
    
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=512)
    year = models.IntegerField()
    rated = models.CharField(max_length=512)
    released = models.CharField(max_length=512)
    runtime = models.CharField(max_length=512)
    genre = models.CharField(max_length=512)
    director = models.CharField(max_length=512)
    writer = models.CharField(max_length=512)
    actors = models.CharField(max_length=512) 
    plot = models.CharField(max_length=1024)
    language = models.CharField(max_length=512)
    country = models.CharField(max_length=512)
    awards = models.CharField(max_length=512)
    poster = models.CharField(max_length=512)
    metascore = models.CharField(max_length=512)
    imdbrating = models.CharField(max_length=512)
    imdbvotes = models.CharField(max_length=512)
    imdbid = models.CharField(max_length=512)
    type = models.CharField(max_length=512)
    dvd= models.CharField(max_length=512) 
    boxoffice = models.CharField(max_length=512)
    production = models.CharField(max_length=512)
    website = models.CharField(max_length=512)
    response= models.CharField(max_length=512)
    
    def __str__(self):
        return self.title


class Rating(models.Model):
    source = models.CharField(max_length=128)
    value =  models.CharField(max_length=128)
    movie = models.ForeignKey(MovieData, on_delete=models.CASCADE, to_field='id', db_column='title')


class Comment(models.Model):
    comment = models.CharField(max_length=128)
    movie = models.ForeignKey(MovieData, on_delete=models.CASCADE, to_field='id', db_column='title',related_name='comm')

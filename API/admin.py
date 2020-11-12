from django.contrib import admin
from .models import MovieData,Rating,Comment

# Register your models here.

class MovieDataAdmin(admin.ModelAdmin):
    fields = ['title', 'year', 'rated', 'released', 'runtime']
admin.site.register(MovieData, MovieDataAdmin)

class RatingAdmin(admin.ModelAdmin):
    fields = ['source','value', 'movie']
admin.site.register(Rating, RatingAdmin) 

class CommentAdmin(admin.ModelAdmin):
    fields = ['comment','movie']
admin.site.register(Comment, CommentAdmin)




from django.urls import path
from API import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('movies/', views.MovieDetails.as_view(), name = 'movie_detail'),
    path('movies/<int:pk>/', views.MovieDetailModify.as_view(), name='movie_modify'),
    path('comments/', views.MovieDetailComment.as_view(), name='movie_comment'),
    path('top/', views.MovieTop.as_view(), name='movie_top'),
]   
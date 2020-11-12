import json
import collections

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import MovieData, Comment
from .serializers import MovieDataSerializer

# Create your tests here.

class SortingAndFilterTestCase(APITestCase):
    """
    Separate class for testing sorting and filtering
    """
    def setUp(self):
        
        MovieData.objects.create(title = 'shrek',year = 1999, rated='PG',genre='Animation, Adventure, Comedy, Family, Fantasy',)
        MovieData.objects.create(title = 'titanic',year = 1989, rated='PG',genre='Romantic, Drama, Action')
        MovieData.objects.create(title = 'mask',year = 1975, rated='PG',genre='Action,Comedy')

    # GET SORT
    def test_correct_sorting(self):
        data = {'order_by':'year'}
        response = self.client.generic(method='GET', path="/movies/", data=json.dumps(data), content_type='application/json')
        correct_response = [
            collections.OrderedDict({
                'title':'mask',
                'year':1975,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : 'Action,Comedy',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''
            }),
            collections.OrderedDict({
                'title':'titanic',
                'year':1989,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : 'Romantic, Drama, Action',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''
            }),

            collections.OrderedDict({
                'title':'shrek',
                'year':1999,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : 'Animation, Adventure, Comedy, Family, Fantasy',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''
            }),


        ]
        
        self.assertEqual(response.data, correct_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # GET FILTER
    def test_correct_filter(self):
        data = {'filter_field':'genre', 'filter_value':'Action'}
        response = self.client.generic(method='GET', path="/movies/", data=json.dumps(data), content_type='application/json')
        
        correct_response = [
            
            collections.OrderedDict({
                'title':'titanic',
                'year':1989,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : 'Romantic, Drama, Action',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''
            }),
            collections.OrderedDict({
                'title':'mask',
                'year':1975,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : 'Action,Comedy',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''
            }),
            
        ]
        self.assertEqual(response.data, correct_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #GET SORT + FILTER
    def correct_sorting_filtering(self):
        data = {'filter_field':'genre', 'filter_value':'Action', 'order_by':'year'}
        response = self.client.generic(method='GET', path="/movies/", data=json.dumps(data), content_type='application/json')

        correct_response = [
            
            collections.OrderedDict({
                'title':'mask',
                'year':1975,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : 'Action,Comedy',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''
            }),
            collections.OrderedDict({
                'title':'titanic',
                'year':1989,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : 'Romantic, Drama, Action',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''
            }),
            
        ]

        self.assertEqual(response.data, correct_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class InputDataTestCase(APITestCase):
    
    """
    Class for obtaining data from server and 
    """

    def setUp(self):
        self.movie = MovieData.objects.create(title = 'shrek',year = 1000, rated='PG',)
        self.movie1 = MovieData.objects.create(title = 'shrek2',year = 1000, rated='PG')


    # POST 

    def test_correctly_capture_data_from_server(self):

        data = {'title':'shrek'}

        response = self.client.post(reverse("movie_detail"), data)
        correct_response_data = {'Title': 'Shrek', 
                                'Year': '2001', 
                                'Rated': 'PG', 
                                'Released': '18 May 2001', 
                                'Runtime': '90 min', 
                                'Genre': 'Animation, Adventure, Comedy, Family, Fantasy', 
                                'Director': 'Andrew Adamson, Vicky Jenson', 
                                'Writer': 'William Steig (based upon the book by), Ted Elliott, Terry Rossio, Joe Stillman, Roger S.H. Schulman, Cody Cameron (additional dialogue), Chris Miller (additional dialogue), Conrad Vernon (additional dialogue)', 
                                'Actors': 'Mike Myers, Eddie Murphy, Cameron Diaz, John Lithgow', 
                                'Plot': 'A mean lord exiles fairytale creatures to the swamp of a grumpy ogre, who must go on a quest and rescue a princess for the lord in order to get his land back.', 
                                'Language': 'English', 
                                'Country': 'USA', 
                                'Awards': 'Won 1 Oscar. Another 38 wins & 60 nominations.', 
                                'Poster': 'https://m.media-amazon.com/images/M/MV5BOGZhM2FhNTItODAzNi00YjA0LWEyN2UtNjJlYWQzYzU1MDg5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 
                                'Ratings': [
                                    {'Source': 'Internet Movie Database', 'Value': '7.8/10'}, 
                                    {'Source': 'Rotten Tomatoes', 'Value': '88%'}, 
                                    {'Source': 'Metacritic', 'Value': '84/100'}], 
                                'Metascore': '84', 
                                'imdbRating': '7.8', 
                                'imdbVotes': '604,671', 
                                'imdbID': 'tt0126029', 
                                'Type': 'movie', 
                                'DVD': 'N/A', 
                                'BoxOffice': 'N/A', 
                                'Production': 'DreamWorks SKG, Pacific Data Images (PDI)', 
                                'Website': 'N/A', 
                                'Response': 'True', 
                                'database_ID': 3}
        
        self.assertEqual(response.data, correct_response_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED )

    def test_wrong_capture_data_from_server_no_data(self):

        data = {}
        response = self.client.post(reverse("movie_detail"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_capture_data_from_server_wrong_data(self):

        data = {"id":4}
        response = self.client.post(reverse("movie_detail"), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_getting_list_of_movies(self):
        
        correct_response_data = [
            
            collections.OrderedDict({
                'title':'shrek',
                'year':1000,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : '',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''

            }),
            collections.OrderedDict({
                'title':'shrek2',
                'year':1000,
                'rated':'PG',
                'released' : '',
                'runtime' : '',
                'genre' : '',
                'director' : '',
                'writer' : '',
                'actors' :'',
                'plot' : '',
                'language' :'' ,
                'country' : '',
                'awards' : '',
                'poster' : '',
                'metascore' : '',
                'imdbrating' :'',
                'imdbvotes' : '',
                'imdbid' : '',
                'type' : '',
                'dvd':  '',
                'boxoffice' :'' ,
                'production' :'' ,
                'website' : '',
                'response': ''

            })
        ]    


        response = self.client.get(reverse('movie_detail'))
        self.assertEqual(response.data, correct_response_data)


class DataModifyTestCase(APITestCase):

    """
    Class for testing delete and put request
    """

    # SETUP
    def setUp(self):
        
        self.movie = MovieData.objects.create(title = 'shrek',year = 1000, rated='PG') 
    # DELETE    
    def test_correct_remove_data(self):

        response = self.client.delete('/movies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_id_remove_data(self):
        
        response = self.client.delete('/movies/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_title_not_id_delete(self):

        response = self.client.delete('/movies/shrek/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    # PUT
    def test_succes_update_year(self):
        
        data = {'field':'year'}
        response = self.client.put('/movies/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_no_field_error(self):
        
        data = {'field':'groupie'}
        response = self.client.put('/movies/1/', data)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_error_no_data(self):
        data = {}
        response = self.client.put('/movies/1/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DataCommentViewTestCase(APITestCase):
    
    """
    Class for testing view and add comments
    """


    # SETUP
    def setUp(self):
        self.movie = MovieData.objects.create(title = 'shrek',year = 1000, rated='PG')
        self.comment1 = Comment.objects.create(movie = self.movie, comment ='comment_test_1')
        self.comment2 = Comment.objects.create(movie = self.movie, comment ='comment_test_2')

        self.movie1 = MovieData.objects.create(title = 'shrek2',year = 1000, rated='PG')
        self.comment1 = Comment.objects.create(movie = self.movie1,comment= 'comment_test_1')
        self.comment2 = Comment.objects.create(movie = self.movie1,comment= 'comment_test_2')
        

    # GET 
    def test_correct_get_all_comments(self):

        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_correct_comment_from_one_movie(self):
        data = {'id':2}

        response = self.client.generic(method='GET', path="/comments/", data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    


    # POST

    def test_correct_comment_append(self):

        data = {'id':1, 'comment':'tete'}
        correct_return = { 'comment':'tete'}
        response = self.client.post('/comments/', data)

        self.assertEqual(response.data, correct_return)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_comment_append_no_data(self):
        response = self.client.post('/comments/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_error_comment_append_missing_id(self):
        response = self.client.post('/comments/?comment=tete')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_error_comment_append_missing_comment(self):
        response = self.client.post('/comments/?id=1')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DataTopViewTestCase(APITestCase):

    """
    Class for tesintg top 3 view
    """

    # SETUP 
    def setUp(self):
        self.movie = MovieData.objects.create(title = 'shrek',year = 1000, rated='PG')
        self.comment1 = Comment.objects.create(movie = self.movie, comment ='comment_test_1')
        self.comment2 = Comment.objects.create(movie = self.movie, comment ='comment_test_2')

        self.movie1 = MovieData.objects.create(title = 'shrek2',year = 1000, rated='PG')
        self.comment1 = Comment.objects.create(movie = self.movie1,comment= 'comment_test_1')
        self.comment2 = Comment.objects.create(movie = self.movie1,comment= 'comment_test_2')
        self.comment3 = Comment.objects.create(movie = self.movie1,comment= 'comment_test_3')
        
        self.movie1 = MovieData.objects.create(title = 'shrek3',year = 1000, rated='PG')
        self.comment1 = Comment.objects.create(movie = self.movie1,comment= 'comment_test_1')
        self.comment2 = Comment.objects.create(movie = self.movie1,comment= 'comment_test_2')
        self.comment3 = Comment.objects.create(movie = self.movie1,comment= 'comment_test_3')

    # GET     
    def test_correct_get_top_3_with_range(self):
        

        correct_out = [
            {
                'movie_id': 2, 
                'total_comments': 3, 
                'rank': 1
            },
            {
                'movie_id': 3,
                'total_comments': 3, 
                'rank': 1
            },
            {
                'movie_id': 1,
                'total_comments': 2,
                'rank': 2
            }
                    ]
        
        data = {'from':'1000', 'to':'2000'}
        response = self.client.generic(method='GET', path="/top/", data=json.dumps(data), content_type='application/json')
       
        self.assertEqual(response.data, correct_out)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    


    def test_wrong_get_top_3_no_range(self):
        response = self.client.get('/top/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


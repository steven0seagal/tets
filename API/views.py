import operator

import requests
from django.conf import settings
from django.db.models import Count, F
from django.http import Http404
from django.shortcuts import render
from rest_framework import request, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Comment, MovieData, Rating
from .scripts import object_mod
from .serializers import MovieDataSerializer, MovieDetailCommentSerializer

api_key = getattr(settings, "API_KEY", None)


class MovieDetails(APIView):
    """
    Class that contains function to correctly create data into MovieData database and later recive by id
    """

    def get(self, request, format=None):
        
        "Function for GET method, if contains correct filter and/or grouping parameters, will take them into account otherwise return whole database"
        
        # FILTER and GROUPING
        if 'filter_field' in request.data and 'filter_value' in request.data and 'order_by' in request.data:
            
            movies = MovieData.objects.order_by(request.data['order_by'])
            serializer = MovieDataSerializer(movies, many=True)
            filtered_data = []
            
            for film in serializer.data:
                if request.data['filter_value'] in film[request.data['filter_field']]:
                    filtered_data.append(film)
            return Response(filtered_data, status=status.HTTP_200_OK)

        # FILTER
        elif 'filter_field' in request.data and 'filter_value' in request.data :
            
            movies = MovieData.objects.all()
            serializer = MovieDataSerializer(movies, many=True)
            filtered_data = []
            
            for film in serializer.data:
                if request.data['filter_value'] in  film[request.data['filter_field']]:
                    filtered_data.append(film)
            return Response(filtered_data, status=status.HTTP_200_OK)
        
             
        # GROUPING
        elif 'order_by' in request.data:
            
            movies = MovieData.objects.order_by(request.data['order_by'])
            serializer = MovieDataSerializer(movies, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # WHOLE DATABASE   
        else: 
            movies = MovieData.objects.all()

            serializer = MovieDataSerializer(movies, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):

        "Function for POST method, require title in body and download data from OMDBAPI server"
        
        # param checking        
        if 'title' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # collectiong data
        response  = requests.get('http://www.omdbapi.com/?apikey={}&t={}'.format(api_key,request.data['title']))
        recived_data = response.json()
        
        # creating new objects
        ready_data = {}
        for k,v in recived_data.items():
            if k != "Ratings":
                ready_data[k.lower()] = v
            if k =='Year':
                ready_data[k.lower()] = int(v)

        serializer = MovieDataSerializer(data =ready_data)

        if serializer.is_valid():
            
            obj = serializer.save()
            
            recived_data['database_ID'] = obj.id
            for source,value in recived_data["Ratings"]:
                new_rate = Rating(source=source,value=value, movie = obj)
                new_rate.save()


            return Response(recived_data, status=status.HTTP_201_CREATED)
        # if serializer in not valid 400
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MovieDetailModify(APIView):
    """
    Class that contains function to delete or update MovieData objects database 
    """
    # get object or 404
    def get_object(self, pk):
        try:
            return MovieData.objects.get(pk=pk)
        except MovieData.DoesNotExist:
            raise Http404

    # DELETE
    def delete(self,request,pk,format=None):

        "Function that delete object by its id (required)"

        found_movie = self.get_object(pk)
        found_movie.delete()

        return Response(status=status.HTTP_200_OK)

    # PUT
    def put(self,request,pk,format=None):
        
        "Function that updates MovieData object by id and field to update"

        if 'field' in request.data:

            found_movie = self.get_object(pk)
            response  = requests.get('http://www.omdbapi.com/?apikey={}&t={}'.format(api_key,found_movie))
            recived_data = response.json()
            result = object_mod(found_movie, request.data['field'], recived_data)
            if result is True :
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
class MovieDetailComment(APIView):

    # get object or 404
    def get_object(self, pk):
        try:
            return MovieData.objects.get(pk=pk)
        except MovieData.DoesNotExist:
            raise Http404
    
    # GET 
    def get(self,request,form=None):

        "Function that return comments by movie id if id not provided return whole database"

        if 'id' in request.data:
            movie = self.get_object(pk=request.data['id'])
            comments = Comment.objects.filter(movie=movie)
        else: 
            comments = Comment.objects.all()
        

        serializer = MovieDetailCommentSerializer(comments, many=True)
        list_of_comments = {'comments':[]}
        for i in serializer.data:
            list_of_comments['comments'].append(i['comment'])

        return Response(list_of_comments, status=status.HTTP_200_OK)

    # POST
    def post(self,request,form=None):

        "Function that post comment by movie id"

        if 'id' not in request.data and 'comment' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        movie = self.get_object(request.data['id'])
        
        ready_data = {
            'comment':request.data['comment']
        }
        new_comment = Comment(movie=movie, comment=request.data['comment'])
        
        new_comment.save()

        return Response(ready_data, status=status.HTTP_200_OK)


class MovieTop(APIView):
    """
    Class that contain function to generate top 3 movies in database based on data range
    """


    def get(self,request,format=None):  
        
        "Function that return top 3 movies in release year range"

        classification = {}
        ready_data = []

        if 'from' in request.data and 'to' not in request.data:
            movies = MovieData.objects.filter(year__gte=int(request.data['from']))

        elif 'to' in request.data and 'from' not in request.data:
            movies = MovieData.objects.filter(year__lte=int(request.data['to']))

        elif 'to' in request.data and 'from' in request.data: 
            if int(request.data['from']) > int(request.data['to']):
                return Response(status=status.HTTP_400_BAD_REQUEST) 

            movies = MovieData.objects.filter(year__gte=int(request.data['from']),year__lte=int(request.data['to']))
  
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
                
        for i in movies:

            movie_comments = i.comm.all()

            classification[i.id] = len(movie_comments)        
        
        sorted_d = dict( sorted(classification.items(), key=operator.itemgetter(1),reverse=True))

        rank = 1
        currnet_comm_len = max(classification.values())
       
        for movie_id, comm_number in sorted_d.items():
            if comm_number == currnet_comm_len:
                ready_data.append({'movie_id':movie_id, 'total_comments':comm_number, 'rank':rank})
            elif comm_number < currnet_comm_len:
                rank +=1
                if rank >3:
                    break
        
                currnet_comm_len = comm_number
                ready_data.append({'movie_id':movie_id, 'total_comments':comm_number, 'rank':rank})
                       
            if rank >3:
                break
        
   
        return Response(ready_data, status=status.HTTP_200_OK)



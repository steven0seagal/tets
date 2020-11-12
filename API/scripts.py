from rest_framework import status
from rest_framework.response import Response

def object_mod(single_object,field, new_dataset):

    if field == 'year':
                single_object.year = int(new_dataset['Year'])
                single_object.save()

    elif field == 'rated':
        single_object.rated = new_dataset['Rated']
        single_object.save()

    elif field == 'released':
        single_object.rated = new_dataset['Released']
        single_object.save()

    elif field == 'runtime':
        single_object.rated = new_dataset['Runtime']
        single_object.save()

    elif field == 'genre':
        single_object.rated = new_dataset['Genre']
        single_object.save()

    elif field == 'director':
        single_object.rated = new_dataset['Director']
        single_object.save()

    elif field == 'writer':
        single_object.rated = new_dataset['Writer']
        single_object.save()

    elif field == 'actors':
        single_object.rated = new_dataset['Actors']
        single_object.save()

    elif field == 'plot':
        single_object.rated = new_dataset['Plot']
        single_object.save()
    
    elif field == 'language':
        single_object.rated = new_dataset['Language']
        single_object.save()
    
    elif field == 'country':
        single_object.rated = new_dataset['Country']
        single_object.save()
    
    elif field == 'awards':
        single_object.rated = new_dataset['Awards']
        single_object.save()
    
    elif field == 'poster':
        single_object.rated = new_dataset['Poster']
        single_object.save()

    elif field == 'metascore':
        single_object.rated = new_dataset['Metascore']
        single_object.save()

    elif field == 'imdbrating':
        single_object.rated = new_dataset['imdbRating']
        single_object.save()

    elif field == 'imdbvotes':
        single_object.rated = new_dataset['imdbVotes']
        single_object.save()

    elif field == 'imdbid':
        single_object.rated = new_dataset['imdbID']
        single_object.save()

    elif field == 'type':
        single_object.rated = new_dataset['Type']
        single_object.save()
    elif field == 'dvd':
        single_object.rated = new_dataset['DVD']
        single_object.save()

    elif field == 'boxoffice':
        single_object.rated = new_dataset['BoxOffice']
        single_object.save()
    elif field == 'production':
        single_object.rated = new_dataset['Production']
        single_object.save()
    elif field == 'website':
        single_object.rated = new_dataset['Website']
        single_object.save()
    elif field == 'response':
        single_object.rated = new_dataset['Response']
        single_object.save()
    else:
        return False
    return True
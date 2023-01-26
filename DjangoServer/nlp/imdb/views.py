

from rest_framework.decorators import api_view
from rest_framework.response import Response
from nlp.imdb.services import NaverMovieService

@api_view(['POST'])
def imdb(request):
    # sentence = request.GET
    # print(request.GET)
    print(request.data)
    navermovie = NaverMovieService().hook(request.data['string'])
    print(navermovie)
    return Response({'data' : navermovie})


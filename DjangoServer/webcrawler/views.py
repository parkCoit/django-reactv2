from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from webcrawler.services import ScrapServeice


@api_view(['GET'])
@parser_classes([JSONParser])
def webcrawler(request):
    result = ScrapServeice().naver_movie_review()
    return JsonResponse({'data' : result})
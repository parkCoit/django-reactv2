from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from multiplex.movies.services import DcGan




@api_view(['POST'])
@parser_classes([JSONParser])
def fake_faces(request):
    DcGan().generate_fake_faces()
    print(f'Enter Blog-Login with {request}')
    return JsonResponse({'Response Test' : 'SUCCESS'})


from rest_framework.decorators import api_view
from rest_framework.response import Response

from nlp.korean_classify.services import KoreanClassifyService


@api_view(['POST'])
def koreanClassify(request):
    # sentence = request.GET
    # print(request.GET)
    print(request.data)
    koreanclassify = KoreanClassifyService().hook(request.data['string'])
    return Response({'data' : koreanclassify})


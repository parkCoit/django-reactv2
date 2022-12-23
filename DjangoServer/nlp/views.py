from rest_framework.decorators import api_view
from rest_framework.response import Response
from nlp.samsung_report.samsung_report import Controller

@api_view(['GET'])
def samsung_report(request):
    a = Controller().data_analysis()
    return Response({'data' : a})
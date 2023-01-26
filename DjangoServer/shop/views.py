from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from tensorboard.compat import tf

from dlearn.iris.iris_service import IrisService


@api_view(['POST'])
@parser_classes([JSONParser])
def iris(request):
    user_info = request.data
    sepalLengthCm = tf.constant(float(user_info['SepalLengthCm']))
    sepalWidthCm = tf.constant(float(user_info['SepalWidthCm']))
    setalLengthCm = tf.constant(float(user_info['PetalLengthCm']))
    setalWidthCm = tf.constant(float(user_info['PetalWidthCm']))
    features = [sepalLengthCm, sepalWidthCm, setalLengthCm, setalWidthCm]
    result = IrisService().service_model(features)
    print(type(result))
    print(f'result : {result}')
    print(f'넘어온 데이터 {user_info}')
    print(f'SepalLengthCm : {sepalLengthCm}')
    print(f'SepalWidthCm : {sepalWidthCm}')
    print(f'PetalLengthCm : {setalLengthCm}')
    print(f'PetalWidthCm : {setalWidthCm}')
    if result == 0:
        result = 'setosa / 부채붓꽃'
    elif result == 1:
        result = 'versicolor / 버시칼라 '
    elif result == 2:
        result = 'virginica / 버지니카'
    return JsonResponse({'result' : result})
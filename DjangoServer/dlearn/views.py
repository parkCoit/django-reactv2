import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from tensorboard.compat import tf

from dlearn.iris.fashion_service import FashionService
from dlearn.iris.iris_service import IrisService
from dlearn.number.number_service import NumberService

# iris
@api_view(['GET','POST'])
@parser_classes([JSONParser])
def iris(request):
    if request.method == 'GET':
        print(f" ##### GET at Here React ID is {request.GET['req']} and {request.GET}#####")
        print(f"##### 아아아아아 { [request.GET['req']]}")
        print(f"##### 아아아아아 {request.GET['req']}")
        a = list(request.GET['req'])
        print(type(a))
        a.remove(',')
        a.remove(',')
        a.remove(',')
        a = [float(i) for i in a]
        print(f'##########################{a}')
        result = IrisService().service_model(a)
        if result == 0:
            result = 'setosa / 부채붓꽃'
        elif result == 1:
            result = 'versicolor / 버시칼라 '
        elif result == 2:
            result = 'virginica / 버지니카'
        return JsonResponse({'result' : result})
    elif request.method == 'POST':
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
    else : print(';;;')


# fashion
@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def fashion(request):
    if request.method == 'GET':
        print(f" ##### GET at Here React ID is {request.GET['id']} and {request.GET}#####")
        return JsonResponse({
            'result': FashionService().service_model(int(request.GET['id']))})
    elif request.method == 'POST':
        print(" ##### POST at Here #####")
        body = request.body  # byte string of JSON data
        data = request.data
        print(f" ##### request data is {data} type {type(data)} #####")
        print(f" ##### request body is {body} type {type(body)}#####")
        data = json.loads(body)
        print(request.headers)
        print(request.content_type)
        print(f"##### React ID Is {data} ####")
        result = FashionService().service_model(int(data['Num']))
        return JsonResponse({'result': result})

    else: print(';;;;')


# number
@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def number(request):
    if request.method == 'GET':
        print(f" ##### GET at Here React ID is {request.GET['req']} and {request.GET}#####")
        return JsonResponse({
            'result': str(NumberService().service_model(int(request.GET['req'])))})
    elif request.method == 'POST':
        data = json.loads(request.body)
        result = NumberService().service_model(int(data['Num']))
        return JsonResponse({'result': result})
    else: print(';;;;')


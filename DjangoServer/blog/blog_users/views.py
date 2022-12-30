from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from blog.blog_users.repositories import UserRepository
from blog.blog_users.serializers import UserSerializer


@api_view(['POST', 'GET', 'PUT', 'PATCH','DELETE'])
@parser_classes([JSONParser])
def user(request):
    if request.method == "POST":
        new_user = request.data
        serializer = UserSerializer(data=new_user)
        print(f"리액트에서 등록한 신규 사용자 {new_user}")
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"result" : "SUCCESS"})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        return JsonResponse(UserRepository().find_user_by_email(request.data["user_email"]))

    elif request.method == "PUT":
        repo = UserRepository()
        modify_user = repo.find_user_by_email(request.data["user_email"])
        db_user = repo.find_by_id(modify_user.id)
        serializer = UserSerializer(data=db_user)
        if serializer.is_valid():
            serializer.update(modify_user, db_user)
            return JsonResponse({"result": "SUCCESS"})

        return UserSerializer().update(request.data)
    elif request.method == "PATCH":
        return None

    elif request.method == "DELETE":
        repo = UserRepository()
        delete_user = repo.find_user_by_email(request.data["user_email"])
        db_user = repo.find_by_id(delete_user.id)
        db_user.delete()
        return JsonResponse({"result": "SUCCESS"})


@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request):
    return UserRepository().get_all()


@api_view(['GET'])
@parser_classes([JSONParser])
def user_list_by_name(request):
    return UserRepository().find_user_by_email(request.data['user_name'])


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request): return UserRepository().login(request.data)


@api_view(['POST'])
@parser_classes([JSONParser])
def signup(request):
    user_info = request.data
    email = user_info['email']
    password = user_info['password']
    nickname = user_info['nickname']
    print(f'리엑트에서 보낸 데이터: {user_info}')
    print(f'넘어온 이메일 : {email}')
    print(f'넘어온 비밀번호 : {password}')
    print(f'넘어온 닉네임 : {nickname}')
    return JsonResponse({'로그인 결과': '성공 !'})



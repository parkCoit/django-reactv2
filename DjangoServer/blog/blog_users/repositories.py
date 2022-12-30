from django.http import JsonResponse
from rest_framework.response import Response

from blog.blog_users.models import User
from blog.blog_users.serializers import UserSerializer


class UserRepository(object):

    def __init__(self):
        pass

    def get_all(self):
        return Response(UserSerializer(User.objects.all(), many=True).data)

    def find_by_id(self, id):
        return User.objects.all().filter(id=id).values()[0]

    def find_user_by_email(self, user_email):
        return User.objects.all().filter(user_email=user_email).values()[0]

    def find_user_by_name(self, user_name):
        return User.objects.all().filter(user_name=user_name).values()


    def login(self, arg):  # **kwargs 받아 올때 지정 해줘야함
        try:
            loginUser = User.objects.get(user_email=arg['user_email'])
            print(f"해당 email 을 가진  User ID: *** \n {loginUser.id}")
            if loginUser.password == arg["password"]:
                dbUser = self.find_by_id(loginUser.id)
                print(f" DBUser is {dbUser}")
                serializer = UserSerializer(dbUser, many=False)
                return JsonResponse(data=serializer.data, safe=False)
            else: return Response('..')
        except:
            return JsonResponse({"data": "이메일이 틀립니다"})

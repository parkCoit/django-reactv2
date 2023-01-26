from django.http import JsonResponse
from rest_framework.response import Response

from shop.carts.models import Cart
from shop.carts.serializers import CartSerializer


class CartRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(CartSerializer(Cart.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(CartSerializer(Cart.objects.all(), many=True).data)


from django.http import JsonResponse
from rest_framework.response import Response

from shop.orders.models import Order
from shop.orders.serializers import OrderSerializer


class OrderRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(OrderSerializer(Order.objects.all(), many=True).data)

    def find_by_id(self):
            return Response(OrderSerializer(Order.objects.all(), many=True).data)


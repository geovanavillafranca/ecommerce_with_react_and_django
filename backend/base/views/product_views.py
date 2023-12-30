from typing import Any, Dict
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response
from ..products import products

from django.contrib.auth.models import User

from ..models import *
from ..serializers import ProductSerializer


from rest_framework import status



@api_view(["GET"])
def getProducts(request):

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProduct(request, pk):

    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)
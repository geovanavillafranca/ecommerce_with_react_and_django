from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products

from .models import *
from .serializers import ProductSerializer

# Create your views here.
@api_view(["GET"])
def getRoutes(request):
    return Response('Hello')

@api_view(["GET"])
def getProducts(request):
    # if request.method == 'POST':
    #     p =Product.objects.create(
    #         name=request.data['name'],
    #         description=request.data['description'],
    #         brand=request.data['brand'],
    #         category=request.data['category'],
    #         price=request.data['price'],
    #         countInStock=request.data['countInStock'],
    #         rating=request.data['rating'],
    #         numReviews=request.data['numReviews'],
    #         )
    #     print(p)
    #     return Response({"message": "Got some data!", "data": request.data})

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getProduct(request, pk):

    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


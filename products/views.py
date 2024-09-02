from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serialize import ProductSerializer

# Create your views here.
@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    json_response = serializer.data
    return Response(json_response)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/products/',
        '/api/product/<id>',
    ]
    return Response(routes)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

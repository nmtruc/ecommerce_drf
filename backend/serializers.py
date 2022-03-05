from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

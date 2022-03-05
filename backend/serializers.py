from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product


class UserSerializer(ModelSerializer):
    _id = SerializerMethodField(read_only=True)
    name = SerializerMethodField(read_only=True)
    isAdmin = SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', '_id', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

    def get_isAdmin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', '_id', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

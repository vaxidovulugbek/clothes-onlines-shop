from datetime import datetime

from rest_framework import serializers

from accountapp.models import CustomUser
from productapp.models import Category, Color, Size, Product
from orderapp.models import Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    amountOfProduct = serializers.SerializerMethodField(method_name='getAmountOfProduct')

    class Meta:
        model = Category
        fields = ('id', 'name', 'amountOfProduct')

    def getAmountOfProduct(self, obj):
        return obj.getAmountOfProduct


class ColorSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Color
        fields = ('id', 'name')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    # color = ColorSerializer(many=True)
    # size = SizeSerializer(many=True)
    # category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'size', 'color']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    totalSumOrder = serializers.SerializerMethodField(method_name='getTotalSumOrder')
    order = OrderSerializer(many=False)
    product = ProductSerializer(many=False)

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price', 'quantity', 'totalSumOrder',)
        # fields = '__all__'

    def getTotalSumOrder(self, obj):
        return obj.getTotalSumOrder


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

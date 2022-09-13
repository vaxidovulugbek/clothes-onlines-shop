import json

from django.contrib.auth import login
from rest_framework import views
from rest_framework.decorators import api_view

from accountapp.models import CustomUser
from utilites.response import response

from orderapp.models import OrderItem, Order
from productapp.models import Product, Category, Color, Size
from .serializers import (ProductSerializer, OrderItemSerializer, CategorySerializer, \
                          ColorSerializer, SizeSerializer, UserSerializer,
                          RegisterSerializer, OrderSerializer, )
from rest_framework.parsers import MultiPartParser, FormParser

from api import serializers


class GetRoutesView(views.APIView):
    def get(self, request):
        routes = [
            {'GET': '/api/categories/'},
            {'GET': '/api/products/'},
            {'GET': '/api/sizes/'},
            {'GET': '/api/colors/'},
            {'GET': '/api/orders/'},
            {'GET': '/api/accounts/register/'},
            {'GET': '/api/accounts/login/'},

            # {'DELETE': '/api/products/id/delete',}
        ]
        return response(data=routes, isBad=False)


class UserRegisterView(views.APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()
            return response(data=serializer.data, isBad=False)
        else:
            data = serializer.errors
            return response(data=data, isBad=True)


class UserLoginView(views.APIView):
    def post(self, request):
        data = {}
        reqBody = json.loads(request.body)
        email = reqBody['email']
        password = reqBody['password']
        account = CustomUser.objects.get(email=email)
        if account:
            if account.is_active:
                login(request, account)
                data["message"] = "user logged in"
                return response(data=data, isBad=False)
            else:
                pass


class CategoryCRUDView(views.APIView):
    """
        Bu view orqali category modeli uchun crud bajariladi
    """

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        getCategoryId = self.request.query_params.get('getCategoryId')
        if getCategoryId is not None:
            category = Category.objects.get(id=getCategoryId)
            serializer = CategorySerializer(category, many=False)
            return response(data=serializer.data, isBad=False)
        else:
            serializer = CategorySerializer(categories, many=True)
            return response(data=serializer.data, isBad=False)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)

    def delete(self, request):
        deleteCategoryId = self.request.query_params.get("deleteCategoryId")
        category = Category.objects.get(id=deleteCategoryId)
        category.delete()
        return response(data="Ma'lumot o'chirildi", isBad=False)

    def patch(self, request):
        patchCategoryId = self.request.query_params.get("patchCategoryId")
        category = Category.objects.get(id=patchCategoryId)
        serializer = CategorySerializer(data=request.data, instance=category)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)


class ProductCRUDView(views.APIView):
    """
        Bu view orqali product modeli uchun crud bajariladi
    """

    def get(self, *args, **kwargs):
        getProductId = self.request.query_params.get('getProductId')
        products = Product.objects.all()
        if getProductId is not None:
            product = Product.objects.get(pk=getProductId)
            serializer = ProductSerializer(product, many=False)
            return response(data=serializer.data, isBad=False)
        else:
            serializer = ProductSerializer(products, many=True)
            return response(data=serializer.data, isBad=False)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)

    def delete(self, request):
        deleteProductId = self.request.query_params.get("deleteProductId")
        try:
            product = Product.objects.get(id=deleteProductId)
            product.delete()
            return response(data="Ma'lumot o'chirildi", isBad=False)
        except Exception as error:
            return response(data=error, isBad=True)

    def patch(self, request):
        patchProductId = self.request.query_params.get("patchProductId")
        product = Product.objects.get(id=patchProductId)
        serializer = ProductSerializer(data=request.data, instance=product)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)


class ColorCRUDView(views.APIView):
    """
        Bu view orqali color modeli uchun crud bajariladi
    """

    def get(self, *args, **kwargs):
        getColorId = self.request.query_params.get('getColorId')
        colors = Color.objects.all()
        if getColorId is not None:
            color = Color.objects.get(pk=getColorId)
            serializer = ColorSerializer(color, many=False)
            return response(data=serializer.data, isBad=False)
        else:
            serializer = ColorSerializer(colors, many=True)
            return response(data=serializer.data, isBad=False)

    def post(self, request):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)

    def delete(self, request):
        deleteColorId = self.request.query_params.get("deleteColorId")
        try:
            color = Color.objects.get(id=deleteColorId)
            color.delete()
            return response(data="Ma'lumot o'chirildi", isBad=False)
        except Exception as e:
            return response(data="Bunday ma'lumot mavjud emas", isBad=True)

    def patch(self, request):
        patchColorId = self.request.query_params.get("patchColorId")
        color = Color.objects.get(id=patchColorId)
        serializer = ColorSerializer(data=request.data, instance=color)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)


class SizeCRUDView(views.APIView):
    """
         Bu view orqali size modeli uchun crud bajariladi
    """

    def get(self, *args, **kwargs):
        getSizeId = self.request.query_params.get('getSizeId')
        sizes = Size.objects.all()
        if getSizeId is not None:
            size = Color.objects.get(pk=getSizeId)
            serializer = ColorSerializer(size, many=False)
            return response(data=serializer.data, isBad=False)
        else:
            serializer = ColorSerializer(sizes, many=True)
            return response(data=serializer.data, isBad=False)

    def post(self, request):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)

    def delete(self, request):
        deleteSizeId = self.request.query_params.get("deleteSizeId")
        size = Size.objects.get(id=deleteSizeId)
        size.delete()
        return response(data="Ma'lumot o'chirildi", isBad=False)

    def patch(self, request):
        patchSizeId = self.request.query_params.get("patchSizeId")
        size = Size.objects.get(id=patchSizeId)
        serializer = ColorSerializer(data=request.data, instance=size)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)


class OrderCRUDView(views.APIView):
    def get(self, request):
        userId = self.request.query_params.get("userId")
        if userId is not None:
            user = CustomUser.objects.get(id=userId)
            orders = user.user_orders.all()
            serializer = OrderSerializer(orders, many=True)
            return response(data=serializer.data, isBad=False)
        return response(data="User not found", isBad=True)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def patch(self, request):
        pass


class OrderItemListView(views.APIView):
    def get(self, *args, **kwargs):
        orderItems = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderItems, many=True)
        orderId = self.request.query_params.get('getOrderId')
        if orderId is not None:
            order = Order.objects.get(id=orderId)
            orderItems = order.items.all()
            serializer = OrderItemSerializer(orderItems, many=True)
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.data, isBad=False)


class OrderItemDetailView(views.APIView):
    def get(self, request, *args, **kwargs):
        orderItem = OrderItem.objects.get(pk=kwargs)
        serializer = OrderItemSerializer(orderItem, many=False)
        return response(data=serializer.data, isBad=False)


class UserListView(views.APIView):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return response(data=serializer.data)

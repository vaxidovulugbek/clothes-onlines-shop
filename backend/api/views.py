import json

from django.contrib.auth import login
from rest_framework import views
from rest_framework.decorators import api_view

from accountapp.models import CustomUser
from utilites.response import response

from orderapp.models import OrderItem, Order
from productapp.models import Product, Category, Color, Size
from .serializers import (ProductSerializer, OrderItemSerializer, CategorySerializer, \
                          ColorSerializer, SizeSerializer, \
                          RegisterSerializer, )
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/categories/'},
        {'GET': '/api/products/'},
        {'GET': '/api/sizes/'},
        {'GET': '/api/colors/'},
        {'GET': '/api/accounts/register/'},
        {'GET': '/api/accounts/login/'},

        # {'DELETE': '/api/products/id/delete',}
    ]
    return response(data=routes, isBad=False)


class GetRoutesView(views.APIView):
    def get(self, request):
        routes = [
            {'GET': '/api/categories/'},
            {'GET': '/api/products/'},
            {'GET': '/api/sizes/'},
            {'GET': '/api/colors/'},
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
            # token = Token.objects.get_or_create(user=account)[0].key
            # data["token"] = token
            return response(data=serializer.data, isBad=False)
        else:
            data = serializer.errors
            return response(data=serializer.data, isBad=True)


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

    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        categoryId = self.request.query_params.get('categoryId')
        if categoryId is not None:
            category = Category.objects.get(id=categoryId)
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
        deleteId = self.request.query_params.get("deleteId")
        category = Category.objects.get(id=deleteId)
        category.delete()
        return response(data="Ma'lumot o'chirildi", isBad=False)

    def patch(self, request):
        categoryId = self.request.query_params.get("patchId")
        category = Category.objects.get(id=categoryId)
        serializer = CategorySerializer(data=request.data, instance=category)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)


class ProductCRUDView(views.APIView):
    parser_classes = MultiPartParser, FormParser
    """
        Bu view orqali product modeli uchun crud bajariladi
    """

    def get(self, *args, **kwargs):
        productId = self.request.query_params.get('productId')
        products = Product.objects.all()
        if productId is not None:
            product = Product.objects.get(pk=productId)
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
        deleteId = self.request.query_params.get("deleteId")
        try:
            product = Product.objects.get(id=deleteId)
            product.delete()
            return response(data="Ma'lumot o'chirildi", isBad=False)
        except Exception as error:
            return response(data=error, isBad=True)

    def patch(self, request):
        patchId = self.request.query_params.get("patchId")
        product = Product.objects.get(id=patchId)
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
        getId = self.request.query_params.get('getId')
        colors = Color.objects.all()
        if getId is not None:
            color = Color.objects.get(pk=getId)
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
        deleteId = self.request.query_params.get("deleteId")
        try:
            color = Color.objects.get(id=deleteId)
            color.delete()
            return response(data="Ma'lumot o'chirildi", isBad=False)
        except Exception as e:
            return response(data="Bunday ma'lumot mavjud emas", isBad=True)

    def patch(self, request):
        patchId = self.request.query_params.get("patchId")
        color = Color.objects.get(id=patchId)
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
        getId = self.request.query_params.get('getId')
        sizes = Size.objects.all()
        if getId is not None:
            size = Color.objects.get(pk=getId)
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
        deleteId = self.request.query_params.get("deleteId")
        size = Size.objects.get(id=deleteId)
        size.delete()
        return response(data="Ma'lumot o'chirildi", isBad=False)

    def patch(self, request):
        patchId = self.request.query_params.get("patchId")
        size = Size.objects.get(id=patchId)
        serializer = ColorSerializer(data=request.data, instance=size)
        if serializer.is_valid():
            serializer.save()
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.errors, isBad=True)


class OrderItemListView(views.APIView):
    def get(self, *args, **kwargs):
        orderItems = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderItems, many=True)
        orderId = self.request.query_params.get('orderId')
        if orderId is not None:
            order = Order.objects.get(id=orderId)
            orderItems = order.items.all()
            serializer = OrderItemSerializer(orderItems, many=True)
            return response(data=serializer.data, isBad=False)
        return response(data=serializer.data, isBad=False)


class OrderItemDetailView(views.APIView):
    def get(self, *args, **kwargs):
        orderItem = OrderItem.objects.get(pk=kwargs)
        serializer = OrderItemSerializer(orderItem, many=False)
        return response(data=serializer.data, isBad=False)

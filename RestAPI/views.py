from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User, auth
from  shop.models import product, imageslider, cart, Order
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from RestAPI.serializers import productSerializer, orderSerializer, userSerializer, loginSerializer
from django.contrib import messages
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
import jwt
# Create your views here.

    # Displaying the products list or creating new products
class productList(APIView):
    def get(self, request):
        products = product.objects.all()
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class productDetails(APIView):
    def get_object(self, id):
        try:
            return product.objects.get(id=id)
        except product.DoesNotExist:
            return HttpResponse (status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        product = self.get_object(id)
        serializer = productSerializer(product)
        return Response(serializer.data)

    # Displaying the Orders lists
class orderDetails(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = orderSerializer(orders, many=True)
        return Response(serializer.data)

    # User List
class userList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = userSerializer(users, many=True)
        return Response(serializer.data)


    # Registration of User
class RegisterView(APIView):
    serializer_class = userSerializer
    def post(self, request):
        serializer = userSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response']= "Your Account is created Successfully"
            token = Token.objects.get(User).key
            data['token'] = token
        else:
            data =serializer.data
        return Response(data)

    # Users Login
class LoginView(APIView):
    serializer_class = loginSerializer
    def post(self, request):
        serializer = loginSerializer(data=request.data)
        user = auth.authenticate(serializer)
        if user is not None:
            auth.login(request, user)
            return Response(user)
        else:
            messages.info(request, 'Password not matching ')
        return Response(status=status.HTTP_200_OK)   
        
    




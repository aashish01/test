from rest_framework import serializers
from  shop.models import product, Order
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username','first_name','last_name','password','email')
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User(
                username=validated_data['username'],
                email=validated_data['email']
            )
            user.set_password(validated_data['password'])
            Token.objects.create(user=user)
            user.save()
            return user

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username', 'password')
        extra_kwargs = {"password": {"write_only": True}}


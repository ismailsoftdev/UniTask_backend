from rest_framework import serializers
from accounts.models import User

class UserSearializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'profile', 'is_active']

class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    full_name = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'full_name', 'password', 'profile']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password']
    

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserSearializer()
    class Meta:
        model = User
        fields = ['token', 'user']

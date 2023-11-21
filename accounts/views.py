from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from accounts.models import User
from accounts import serializers
from accounts.forms import UserForm

class UserProfile(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSearializer
    form_class = UserForm
    permission_classes = [permissions.IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserRegisterSerializer
    #form_class = UserForm
    permission_classes = [permissions.AllowAny]
    

class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSearializer
    form_class = UserForm
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserDeactivate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSearializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'User deactivated successfully.'})

class UserLogin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        username = user['email']
        password = user['password']
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        # create token
        token, created = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'user': serializers.UserSearializer(user).data
        }
        return Response(data, status=status.HTTP_200_OK)
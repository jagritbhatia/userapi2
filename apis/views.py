from rest_framework import generics
from .models import CustomUser
from .serializers import UserCreateSerializer
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'base.html'

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

class UserDelete(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
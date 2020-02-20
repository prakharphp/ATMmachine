# atm/views.py
from rest_framework import generics

from .models import UserAccount
from .serializers import UserAccountSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

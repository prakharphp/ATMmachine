# atm/views.py
from rest_framework import generics
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import UserAccount
from .serializers import UserAccountSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


@csrf_exempt
def deposit(request, card, amount):
    a = UserAccount.objects.get(card_number=card)
    a.amount = a.amount+amount
    a.save()
    serializer = UserAccountSerializer(a)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def withdraw(request, card, amount):
    a = UserAccount.objects.get(card_number=card)
    a.amount = a.amount-amount
    a.save()
    serializer = UserAccountSerializer(a)
    return JsonResponse(serializer.data, safe=False)

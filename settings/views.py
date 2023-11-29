from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
# imort model
from .models import *

# import serializers
from .serializers import *



class reclying_center_view(viewsets.ModelViewSet):
    queryset = Recycling_Center.objects.all()
    serializer_class = recyling_centerserializer


class garbage_type_view(viewsets.ModelViewSet):
    queryset = GarbageType.objects.all()
    serializer_class = garbage_typeserializer


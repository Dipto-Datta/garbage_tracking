from rest_framework import serializers
from .models import *



class recyling_centerserializer(serializers.ModelSerializer):
    class Meta:
        model = Recycling_Center
        fields  ="__all__"


class garbage_typeserializer(serializers.ModelSerializer):
    class Meta:
        model = GarbageType
        fields ="__all__"
from rest_framework import serializers
from .models import HomeDetails


class HomeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeDetails
        fields = '__all__'
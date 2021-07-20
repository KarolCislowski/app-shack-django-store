from django.db.models import fields
from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Product

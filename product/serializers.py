from product.models import *
from rest_framework import serializers




class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetails
        fields =   '__all__'
        # fields =   ['loc_name']


class AmazonSerializer(serializers.ModelSerializer):

    class Meta:
        model = AmazonProduct
        fields =   '__all__'

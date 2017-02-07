from .models import Property, Area, Additional, Adjustment
from rest_framework import serializers


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'


class AdditionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Additional
        fields = '__all__'


class AdjustmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adjustment
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    area = AreaSerializer(required=False, many=True)
    additional = AdditionalSerializer(required=False, many=True)
    adjustment = AdjustmentSerializer(required=False, many=True)

    class Meta:
        model = Property
        fields = '__all__'

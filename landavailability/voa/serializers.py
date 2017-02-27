from .models import Property, Area, Additional, Adjustment
from rest_framework import serializers
from django.db import transaction


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('floor', 'description', 'area', 'price', 'value')


class AdditionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Additional
        fields = ('other_oa_description', 'size', 'price', 'value')


class AdjustmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adjustment
        fields = ('description', 'percent')


class PropertySerializer(serializers.ModelSerializer):
    areas = AreaSerializer(many=True, required=False)
    additionals = AdditionalSerializer(many=True, required=False)
    adjustments = AdjustmentSerializer(many=True, required=False)

    class Meta:
        model = Property
        fields = (
            'uarn', 'assessment_reference', 'ba_code', 'firm_name',
            'number_or_name', 'sub_street_1', 'sub_street_2', 'sub_street_3',
            'street', 'town', 'postal_district', 'county', 'postcode',
            'scheme_ref', 'primary_description', 'total_area', 'subtotal',
            'total_value', 'adopted_rv', 'list_year', 'ba_name',
            'ba_reference_number', 'vo_ref', 'from_date', 'to_date',
            'scat_code_only', 'unit_of_measurement', 'unadjusted_price',
            'adjustement_total_before', 'adjustement_total',
            'areas', 'additionals', 'adjustments')

        # We want to handle duplicated entries manually so we remove the
        # unique validator
        extra_kwargs = {
            'uarn': {
                'validators': [],
            },
            'ba_reference_number': {
                'validators': [],
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        ba_ref = validated_data['ba_reference_number']

        # If the Property already exists, don't create a new object and
        # just update all its fields.
        try:
            prop = Property.objects.get(ba_reference_number=ba_ref)
        except Property.DoesNotExist:
            prop = Property()
            prop.ba_reference_number = ba_ref

        # Set all the fields for the Property object
        prop.uarn = validated_data['uarn']
        prop.assessment_reference = validated_data['assessment_reference']
        prop.ba_code = validated_data['ba_code']
        prop.firm_name = validated_data['firm_name']
        prop.number_or_name = validated_data['number_or_name']
        prop.sub_street_1 = validated_data['sub_street_1']
        prop.sub_street_2 = validated_data['sub_street_2']
        prop.sub_street_3 = validated_data['sub_street_3']
        prop.street = validated_data['street']
        prop.town = validated_data['town']
        prop.postal_district = validated_data['postal_district']
        prop.county = validated_data['county']
        prop.postcode = validated_data['postcode']
        prop.scheme_ref = validated_data['scheme_ref']
        prop.primary_description = validated_data['primary_description']
        prop.total_area = validated_data['total_area']
        prop.subtotal = validated_data['subtotal']
        prop.total_value = validated_data['total_value']
        prop.adopted_rv = validated_data['adopted_rv']
        prop.list_year = validated_data['list_year']
        prop.ba_name = validated_data['ba_name']
        prop.ba_reference_number = validated_data['ba_reference_number']
        prop.vo_ref = validated_data['vo_ref']
        prop.from_date = validated_data['from_date']
        prop.to_date = validated_data['to_date']
        prop.scat_code_only = validated_data['scat_code_only']
        prop.unit_of_measurement = validated_data['unit_of_measurement']
        prop.unadjusted_price = validated_data['unadjusted_price']
        prop.adjustement_total_before = validated_data.get(
            'adjustement_total_before')
        prop.adjustement_total = validated_data.get('adjustement_total')
        prop.save()

        # Clean existing Area objects and create the new ones posted
        Area.objects.filter(area_property__ba_reference_number=ba_ref).delete()

        areas = validated_data.get('areas')
        for area in areas or []:
            Area.objects.create(area_property=prop, **area)

        # Clean existing Adjustment objects and create the new ones posted
        Adjustment.objects.filter(
            adjustment_property__ba_reference_number=ba_ref).delete()

        adjustments = validated_data.get('adjustments')
        for adjustment in adjustments or []:
            Adjustment.objects.create(adjustment_property=prop, **adjustment)

        # Clean existing Additional objects and create the new ones posted
        Additional.objects.filter(
            additional_property__ba_reference_number=ba_ref).delete()

        additionals = validated_data.get('additionals')
        for additional in additionals or []:
            Additional.objects.create(additional_property=prop, **additional)

        return prop

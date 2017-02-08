from .models import Property, Area, Additional, Adjustment
from rest_framework import serializers
from django.db import transaction


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

        # We want to handle duplicated entries manually so we remove the
        # unique validator
        extra_kwargs = {
            'uarn': {
                'validators': [],
            }
        }

    @transaction.atomic
    def create(self, validated_data):
        uarn = validated_data['uarn']

        # If the Property already exists, don't create a new object and
        # just update all its fields.
        try:
            prop = Property.objects.get(uarn=uarn)
        except Property.DoesNotExist:
            prop = Property()
            prop.uarn = uarn

        # Set all the fields for the Property object
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
        prop.scat_code_only = validated_data['scat_code_only']
        prop.unit_of_measurement = validated_data['unit_of_measurement']
        prop.unadjusted_price = validated_data['unadjusted_price']
        prop.adjustement_total_before = validated_data[
            'adjustement_total_before']
        prop.adjustement_total = validated_data['adjustement_total']
        prop.save()

        # Clean existing Area objects and create the new ones posted
        Area.objects.filter(property__uarn=uarn).delete()

        for a in validated_data['area']:
            area = Area()
            area.property = prop
            area.floor = a['floor']
            area.description = a['description']
            area.area = a['area']
            area.price = a['price']
            area.value = a['value']
            area.save()

        # Clean existing Adjustment objects and create the new ones posted
        Adjustment.objects.filter(property__uarn=uarn).delete()

        for a in validated_data['adjustment']:
            adjustment = Adjustment()
            adjustment.property = prop
            adjustment.description = a['description']
            adjustment.percent = a['percent']
            adjustment.save()

        # Clean existing Additional objects and create the new ones posted
        Additional.objects.filter(property__uarn=uarn).delete()

        for a in validated_data['additional']:
            additional = Additional()
            additional.property = prop
            additional.other_oa_description = a['other_oa_description']
            additional.size = a['size']
            additional.price = a['price']
            additional.value = a['value']
            additional.save()

        return prop

from unittest import TestCase
import pytest
import json
from voa.serializers import PropertySerializer
from voa.models import Property, Adjustment, Additional, Area


class TestVOASerializer(TestCase):
    @pytest.mark.django_db
    def test_voa_serializer_valid_payload(self):
        json_payload = """
            {
                "areas": [
                    {
                        "floor": "Ground",
                        "description": "Retail Zone A",
                        "area": 55.50,
                        "price": 265.00,
                        "value": 14708
                    },
                    {
                        "floor": "Ground",
                        "description": "Retail Zone B",
                        "area": 68.93,
                        "price": 132.50,
                        "value": 9133
                    },
                    {
                        "floor": "Ground",
                        "description": "Retail Zone C",
                        "area": 68.93,
                        "price": 66.25,
                        "value": 4567
                    },
                    {
                        "floor": "Ground",
                        "description": "Remaining Retail Zone",
                        "area": 45.21,
                        "price": 33.13,
                        "value": 1498
                    }
                ],
                "additionals": [],
                "adjustments": [
                    {
                        "description": "Bracknell town redevelopment",
                        "percent": -15.00
                    }
                ],
                "assessment_reference": "16656743000",
                "uarn": "6922442000",
                "ba_code": "0335",
                "firm_name": "TRAVEL DOCTOR LTD",
                "number_or_name": "",
                "sub_street_3": "",
                "sub_street_2": "",
                "sub_street_1": "THE GALLERY",
                "street": "PRINCESS SQUARE",
                "town": "",
                "postal_district": "BRACKNELL",
                "county": "BERKS",
                "postcode": "RG12 1LS",
                "scheme_ref": "290405",
                "primary_description": "Shop And Premises",
                "total_area": 238.57,
                "subtotal": 29906,
                "total_value": 25420,
                "adopted_rv": 25250,
                "list_year": 2017,
                "ba_name": "Bracknell Forest",
                "ba_reference_number": "00260500013008",
                "vo_ref": "20976274144",
                "from_date": "01-APR-2017",
                "to_date": "",
                "scat_code_only": "249",
                "unit_of_measurement": "NIA",
                "unadjusted_price": 265.00,
                "adjustement_total_before": 29906,
                "adjustement_total": -4486
            }
        """

        data = json.loads(json_payload)
        serializer = PropertySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    @pytest.mark.django_db
    def test_voa_serializer_create_object(self):
        json_payload = """
            {
                "areas": [
                    {
                        "floor": "Ground",
                        "description": "Retail Zone A",
                        "area": 55.50,
                        "price": 265.00,
                        "value": 14708
                    },
                    {
                        "floor": "Ground",
                        "description": "Retail Zone B",
                        "area": 68.93,
                        "price": 132.50,
                        "value": 9133
                    },
                    {
                        "floor": "Ground",
                        "description": "Retail Zone C",
                        "area": 68.93,
                        "price": 66.25,
                        "value": 4567
                    },
                    {
                        "floor": "Ground",
                        "description": "Remaining Retail Zone",
                        "area": 45.21,
                        "price": 33.13,
                        "value": 1498
                    }
                ],
                "additionals": [],
                "adjustments": [
                    {
                        "description": "Bracknell town redevelopment",
                        "percent": -15.00
                    }
                ],
                "assessment_reference": "16656743000",
                "uarn": "6922442000",
                "ba_code": "0335",
                "firm_name": "TRAVEL DOCTOR LTD",
                "number_or_name": "",
                "sub_street_3": "",
                "sub_street_2": "",
                "sub_street_1": "THE GALLERY",
                "street": "PRINCESS SQUARE",
                "town": "",
                "postal_district": "BRACKNELL",
                "county": "BERKS",
                "postcode": "RG12 1LS",
                "scheme_ref": "290405",
                "primary_description": "Shop And Premises",
                "total_area": 238.57,
                "subtotal": 29906,
                "total_value": 25420,
                "adopted_rv": 25250,
                "list_year": 2017,
                "ba_name": "Bracknell Forest",
                "ba_reference_number": "00260500013008",
                "vo_ref": "20976274144",
                "from_date": "01-APR-2017",
                "to_date": "",
                "scat_code_only": "249",
                "unit_of_measurement": "NIA",
                "unadjusted_price": 265.00,
                "adjustement_total_before": 29906,
                "adjustement_total": -4486
            }
        """

        data = json.loads(json_payload)
        serializer = PropertySerializer(data=data)
        self.assertTrue(serializer.is_valid())

        serializer.save()
        self.assertEqual(Property.objects.count(), 1)
        self.assertEqual(Area.objects.count(), 4)
        self.assertEqual(Adjustment.objects.count(), 1)
        self.assertEqual(Additional.objects.count(), 0)

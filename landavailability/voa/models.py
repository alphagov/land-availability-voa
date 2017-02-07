from django.db import models


class Property(models.Model):
    assessment_reference = models.CharField(
        max_length=32, blank=True, null=True)
    uarn = models.CharField(unique=True, max_length=100)
    ba_code = models.CharField(max_length=255, blank=True, null=True)
    firm_name = models.CharField(max_length=255, blank=True, null=True)
    number_or_name = models.CharField(max_length=255, blank=True, null=True)
    sub_street_1 = models.CharField(max_length=255, blank=True, null=True)
    sub_street_2 = models.CharField(max_length=255, blank=True, null=True)
    sub_street_3 = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    postal_district = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    scheme_ref = models.CharField(max_length=255, blank=True, null=True)
    primary_description = models.CharField(
        max_length=255, blank=True, null=True)
    total_area = models.DecimalField(
        max_digits=16, decimal_places=2, null=True)
    subtotal = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    total_value = models.DecimalField(
        max_digits=16, decimal_places=2, null=True)
    adopted_rv = models.DecimalField(
        max_digits=16, decimal_places=2, null=True)
    list_year = models.IntegerField(null=True)
    ba_name = models.CharField(max_length=255, blank=True, null=True)
    ba_reference_number = models.CharField(
        max_length=255, blank=True, null=True)
    vo_ref = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.CharField(max_length=255, blank=True, null=True)
    to_date = models.CharField(max_length=255, blank=True, null=True)
    scat_code_only = models.CharField(max_length=255, blank=True, null=True)
    unit_of_measurement = models.CharField(
        max_length=255, blank=True, null=True)
    unadjusted_price = models.DecimalField(
        max_digits=16, decimal_places=2, null=True)
    adjustement_total_before = models.DecimalField(
        max_digits=16, decimal_places=2, null=True)
    adjustement_total = models.DecimalField(
        max_digits=16, decimal_places=2, null=True)


class Area(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.SET_NULL, null=True)
    floor = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    area = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    value = models.DecimalField(max_digits=16, decimal_places=2, null=True)


class Adjustment(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    percent = models.DecimalField(max_digits=16, decimal_places=2, null=True)


class Additional(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.SET_NULL, null=True)
    other_oa_description = models.CharField(
        max_length=255, blank=True, null=True)
    size = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    value = models.DecimalField(max_digits=16, decimal_places=2, null=True)

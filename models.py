from django.db import models

class BasicDetails(models.Model):
    property_name = models.CharField(max_length=25)
    manager_name = models.CharField(max_length=25)
    inspected_by = models.CharField(max_length=100)

    def __str__(self):
        return self.property_name


class SafetyDetails(models.Model):
    basic_details = models.OneToOneField(BasicDetails, on_delete=models.CASCADE)
    safe = models.CharField(max_length=50, blank=True)
    Department = models.CharField(max_length=25, blank=True)
    target_correction_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.basic_details.property_name
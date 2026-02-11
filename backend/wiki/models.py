from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="diseases/images/", blank=True, null=True)

    def __str__(self):
        return self.name


class Symptom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="symptoms/images/", blank=True, null=True)
    diseases = models.ManyToManyField(Disease, related_name="symptoms", blank=True)

    def __str__(self):
        return self.name


class RiskFactor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="risk_factors/images/", blank=True, null=True)
    diseases = models.ManyToManyField(Disease, related_name="risk_factors", blank=True)

    def __str__(self):
        return self.name


class Drug(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="drugs/images/", blank=True, null=True)
    diseases = models.ManyToManyField(Disease, related_name="drugs", blank=True)

    def __str__(self):
        return self.name

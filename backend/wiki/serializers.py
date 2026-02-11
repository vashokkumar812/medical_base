from rest_framework import serializers
from .models import Disease, Drug, RiskFactor, Symptom


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ["id", "name", "description", "image", "diseases"]


class RiskFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFactor
        fields = ["id", "name", "description", "image", "diseases"]


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ["id", "name", "description", "image", "diseases"]


class DiseaseSerializer(serializers.ModelSerializer):
    symptoms = SymptomSerializer(many=True, read_only=True)
    risk_factors = RiskFactorSerializer(many=True, read_only=True)
    drugs = DrugSerializer(many=True, read_only=True)

    class Meta:
        model = Disease
        fields = [
            "id",
            "name",
            "description",
            "image",
            "symptoms",
            "risk_factors",
            "drugs",
        ]

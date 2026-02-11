from rest_framework import viewsets
from .models import Disease, Drug, RiskFactor, Symptom
from .serializers import DiseaseSerializer, DrugSerializer, RiskFactorSerializer, SymptomSerializer


class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all().prefetch_related("symptoms", "risk_factors", "drugs")
    serializer_class = DiseaseSerializer


class SymptomViewSet(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer


class RiskFactorViewSet(viewsets.ModelViewSet):
    queryset = RiskFactor.objects.all()
    serializer_class = RiskFactorSerializer


class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

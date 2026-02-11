from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DiseaseViewSet, DrugViewSet, RiskFactorViewSet, SymptomViewSet

router = DefaultRouter()
router.register("diseases", DiseaseViewSet)
router.register("symptoms", SymptomViewSet)
router.register("risk-factors", RiskFactorViewSet)
router.register("drugs", DrugViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from .views import InternBiodataViewset

router = DefaultRouter()

router.register('biodata', InternBiodataViewset)

urlpatterns = router.urls

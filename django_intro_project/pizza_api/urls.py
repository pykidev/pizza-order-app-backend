from rest_framework.routers import DefaultRouter
from .views import PizzaOrderViewset

router = DefaultRouter()

router.register('biodata', PizzaOrderViewset)

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from .views import PizzaOrderViewset, get_csrf_token, PizzaOrderDetailView
from django.urls import path
router = DefaultRouter()

router.register('pizzas', PizzaOrderViewset)

urlpatterns_secondary = [
    path('get_csrf_token/', get_csrf_token, name='get_csrf_token'),
    path('pizzas/order/<int:pk>', PizzaOrderDetailView.as_view(), name='order-detail')
]

urlpatterns  = router.urls + urlpatterns_secondary

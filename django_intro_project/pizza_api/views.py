from rest_framework.viewsets import ModelViewSet
from .models import PizzaOrder
from .serializers import ReadPizzaOrderSerializer, AddPizzaOrderSerializer

class PizzaOrderViewset(ModelViewSet):
    queryset = PizzaOrder.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadPizzaOrderSerializer
        return AddPizzaOrderSerializer
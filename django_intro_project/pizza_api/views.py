from rest_framework.viewsets import ModelViewSet, generics
from .models import PizzaOrder
from .serializers import ReadPizzaOrderSerializer, AddPizzaOrderSerializer, PizzaOrderSerializer
from django.middleware.csrf import get_token
from django.http import JsonResponse

class PizzaOrderViewset(ModelViewSet):
    queryset = PizzaOrder.objects.all().order_by('-id')
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadPizzaOrderSerializer
        return AddPizzaOrderSerializer
        
       
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

class PizzaOrderDetailView(generics.DestroyAPIView):
    queryset = PizzaOrder.objects.all()
    serializer_class = PizzaOrderSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Intern
from .serializers import ReadInternBiodataSerializer, AddInternBiodatSerializer

class InternBiodataViewset(ModelViewSet):
    queryset = Intern.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadInternBiodataSerializer
        return AddInternBiodatSerializer
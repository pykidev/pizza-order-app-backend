from rest_framework import serializers
from .models import Intern

class ReadInternBiodataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ["id", "firstname", "lastname", "email", "university"]
        
class AddInternBiodatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ["firstname", "lastname", "email", "university", "age"]
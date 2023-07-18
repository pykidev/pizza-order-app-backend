from rest_framework import serializers
from .models import PizzaOrder

class ReadPizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ["id", "quantity", "size", "toppings", "add_ons", "delivery"]
        
class AddPizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ["quantity", "size", "toppings", "add_ons", "delivery"]
from django.db import models
from django.utils import timezone

# Create your models here.
class PizzaOrder(models.Model):
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=20)
    toppings = models.CharField(max_length=20)
    add_ons = models.CharField(max_length=20)
    time_of_order = models.DateTimeField(default=timezone.now())
    delivery = models.BooleanField(default=False)
    is_order_ready = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Pizza<[\t\nid:{self.pk}\t\nquantity:{self.quantity}\t\ntoppings:{self.toppings}\t\nsize:{self.size}\t\nadd_ons:{self.add_ons}\t\ntime_of_order:{self.time_of_order}]>"
    
    def is_ready(self):
        return self.is_order_ready
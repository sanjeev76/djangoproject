from django.db import models

# Create your models here.
class Testing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    published_On = models.DateField()

    @property
    def is_in_stock(self):
        return self.quantity  > 0  
from django.db import models
from datetime import datetime 

# Create your models here.
class ExImp(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

    class  Meta:
        verbose_name_plural = 'ExImp'

class Language(models.Model):
    name = models.CharField(max_length=50)
    paradign = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
 
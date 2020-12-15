from django.db import models
from .fibo import Fibonacci
import json
# Create your models here.

class Major(models.Model):
    numero = models.IntegerField()
    calc = Fibonacci(numero)
    json.dumps(calc, default= lambda  x:x.__dict__)

    def __all__(self):
        return self.calc


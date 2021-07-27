from django.db import models
from django.db.models import aggregates

class Employee(models.Model):
    emp_id          = models.IntegerField(primary_key=True)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    age             = models.IntegerField(null=True, default=None)
    phone_number    = models.IntegerField()
    salary          = models.IntegerField()
    city            = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return (self.first_name + " " + self.last_name)
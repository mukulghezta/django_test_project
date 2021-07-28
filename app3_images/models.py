from django.db import models

class Person:
    username    = models.CharField(max_length=100)
    phone       = models.IntegerField()
    pic         = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.username
    

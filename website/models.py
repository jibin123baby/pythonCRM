from django.db import models

# Create your models here.

class customerRecord(models.Model):
    created_At = models.DateTimeField(auto_now_add= True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
from django.db import models

# Create your models here.

class HomeDetails(models.Model):
    uuid = models.AutoField(primary_key=True)
    address_full = models.CharField(max_length=200)
    property_type = models.CharField(max_length=200)
    sewer = models.CharField(max_length=10)
    year_built = models.IntegerField(default=0)

    def __str__(self):
        return self.address_full[:50]
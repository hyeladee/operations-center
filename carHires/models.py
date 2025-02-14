from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    office_address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class CarHire(models.Model):
    STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Processing', 'Processing'),
        ('Awaiting Invoice', 'Awaiting Invoice'),
    )

    passenger_name = models.CharField(max_length=100)
    extra_passengers_name = models.CharField(max_length=200, null=True, blank=True)
    # email = models.EmailField()
    trip_date = models.DateField()
    departure = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='departures')
    destination = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='destinations')
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    trip_cost = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.passenger_name
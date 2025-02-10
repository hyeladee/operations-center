from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    cost_per_night = models.PositiveIntegerField()
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class HotelBooking(models.Model):
    guest_name = models.CharField(max_length=100)
    # email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField(null=True, blank=True)
    hotel_name = models.ForeignKey('Hotel', on_delete=models.PROTECT)
    paid = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def clean(self):
        if self.check_out and self.check_in and self.check_out <= self.check_in:
            raise ValidationError({
                'check_out': _('Check-out date must be after check-in date.')
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.guest_name
    
    class Meta:
        ordering = ['-check_in']  # Most recent bookings first
        verbose_name = 'Hotel Booking'
        verbose_name_plural = 'Hotel Bookings'

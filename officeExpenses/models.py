from django.db import models

# Create your models here.
class ExpenseType(models.Model):
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
    
class OfficeExpense(models.Model):
    STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Processing', 'Processing'),
        ('Awaiting Invoice', 'Awaiting Invoice'),
    )

    description = models.CharField(max_length=100)
    date = models.DateField()
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    cost = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description
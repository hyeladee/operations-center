# Generated by Django 5.1.6 on 2025-02-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelBookings', '0002_remove_hotelbooking_paid_hotelbooking_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='status',
            field=models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Processing', 'Processing'), ('Awaiting Invoice', 'Awaiting Invoice')], max_length=100, null=True),
        ),
    ]

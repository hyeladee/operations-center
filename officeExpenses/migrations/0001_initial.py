# Generated by Django 5.1.6 on 2025-02-13 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('office_address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('cost', models.PositiveIntegerField()),
                ('status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Processing', 'Processing'), ('Awaiting Invoice', 'Awaiting Invoice')], max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('expense_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='officeExpenses.expensetype')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='officeExpenses.vendor')),
            ],
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0006_remove_customer_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(blank=True, choices=[('Collected', 'Collected'), ('Loaded', 'Loaded'), ('Arrived', 'Arrived'), ('Delivered', 'Delivered')], default='Collected', max_length=200, null=True),
        ),
    ]

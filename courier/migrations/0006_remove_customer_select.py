# Generated by Django 3.1.4 on 2020-12-30 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0005_auto_20201229_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='select',
        ),
    ]

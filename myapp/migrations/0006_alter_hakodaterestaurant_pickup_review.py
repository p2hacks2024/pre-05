# Generated by Django 5.1.4 on 2024-12-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_hakodaterestaurant_pickup_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hakodaterestaurant',
            name='pickup_review',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]

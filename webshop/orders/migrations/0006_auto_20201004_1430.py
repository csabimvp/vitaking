# Generated by Django 3.0.10 on 2020-10-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_braintree_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.0.10 on 2020-09-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_same_billing'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
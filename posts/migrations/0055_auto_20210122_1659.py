# Generated by Django 3.1.4 on 2021-01-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0054_auto_20210122_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

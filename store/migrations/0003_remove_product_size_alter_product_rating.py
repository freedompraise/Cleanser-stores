# Generated by Django 4.0.4 on 2022-06-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_customer_product_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]

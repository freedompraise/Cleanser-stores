# Generated by Django 3.0 on 2022-06-21 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20220621_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6),
        ),
    ]
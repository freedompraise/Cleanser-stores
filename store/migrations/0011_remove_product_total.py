# Generated by Django 3.0 on 2022-06-20 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20220620_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total',
        ),
    ]

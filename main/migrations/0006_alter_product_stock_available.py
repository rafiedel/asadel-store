# Generated by Django 5.1.1 on 2024-09-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_available',
            field=models.IntegerField(),
        ),
    ]
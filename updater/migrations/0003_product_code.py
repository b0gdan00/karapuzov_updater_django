# Generated by Django 5.2 on 2025-04-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updater', '0002_alter_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

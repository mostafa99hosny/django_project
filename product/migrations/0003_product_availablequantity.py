# Generated by Django 4.0.4 on 2022-05-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='AvailableQuantity',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
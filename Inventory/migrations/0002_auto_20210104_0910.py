# Generated by Django 3.1 on 2021-01-04 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productname',
            new_name='product',
        ),
    ]

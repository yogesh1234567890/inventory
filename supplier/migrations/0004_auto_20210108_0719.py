# Generated by Django 3.1 on 2021-01-08 07:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_auto_20210108_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.1.3 on 2021-01-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotions', '0002_prediction_t_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='t_label',
            field=models.CharField(max_length=30),
        ),
    ]

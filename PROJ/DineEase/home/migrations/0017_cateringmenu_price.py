# Generated by Django 4.2.4 on 2024-04-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_medicalleave_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='cateringmenu',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]

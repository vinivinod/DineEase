# Generated by Django 4.2.4 on 2024-03-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_catering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catering',
            name='menu_items',
            field=models.ManyToManyField(related_name='catering', to='home.cateringmenu'),
        ),
    ]

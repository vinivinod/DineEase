# Generated by Django 4.2.4 on 2024-03-25 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_catering_menu_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveFromDate', models.DateField()),
                ('leaveToDate', models.DateField()),
                ('reason', models.TextField()),
                ('medicalCertificate', models.FileField(blank=True, null=True, upload_to='medical_certificates')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.2.4 on 2023-10-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="otp",
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name="Otp"),
        ),
    ]

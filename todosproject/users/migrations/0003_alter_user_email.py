# Generated by Django 4.2.4 on 2023-10-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_otp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(blank=True, max_length=255, verbose_name="Email"),
        ),
    ]

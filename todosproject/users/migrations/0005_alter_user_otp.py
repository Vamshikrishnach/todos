# Generated by Django 4.2.4 on 2023-10-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_otp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="otp",
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name="user otp"),
        ),
    ]

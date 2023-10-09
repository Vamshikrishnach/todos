# Generated by Django 4.2.4 on 2023-10-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task1",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("task_name", models.CharField(max_length=20)),
                ("start_date", models.DateField(auto_now=True)),
                ("end_date", models.DateField(auto_now=True)),
                ("status", models.BooleanField()),
            ],
        ),
    ]
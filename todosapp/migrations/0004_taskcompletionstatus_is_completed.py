# Generated by Django 4.2.4 on 2023-10-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todosapp", "0003_taskcompletionstatus"),
    ]

    operations = [
        migrations.AddField(
            model_name="taskcompletionstatus",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
    ]
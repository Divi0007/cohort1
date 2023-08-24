# Generated by Django 4.2.4 on 2023-08-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("batch", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="batches",
            name="status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("waitingapproval", "Waiting approval"),
                    ("active", "Active"),
                    ("ended", "Deleted"),
                ],
                default="active",
                max_length=50,
            ),
        ),
    ]

# Generated by Django 4.1.13 on 2024-01-22 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_post_sub_heading"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.IntegerField(choices=[(0, ""), (1, "Itinerary")], default=0),
        ),
    ]
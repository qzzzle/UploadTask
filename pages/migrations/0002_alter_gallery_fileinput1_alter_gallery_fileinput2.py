# Generated by Django 4.2.6 on 2023-10-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="fileInput1",
            field=models.ImageField(max_length=200, upload_to="pictures/"),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="fileInput2",
            field=models.ImageField(max_length=200, upload_to="pictures/"),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="blog/photo"),
        ),
    ]

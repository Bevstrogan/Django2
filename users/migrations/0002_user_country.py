# Generated by Django 5.0.4 on 2024-05-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(
                default="Не указанно",
                help_text="Введите вашу страну",
                max_length=50,
                verbose_name="Страна",
            ),
        ),
    ]

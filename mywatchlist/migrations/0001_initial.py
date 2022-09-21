# Generated by Django 4.1 on 2022-09-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WatchList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title_movie", models.CharField(max_length=300)),
                ("release_date", models.CharField(max_length=300)),
                ("rating_movie", models.CharField(max_length=300)),
                ("review_movie", models.TextField()),
                ("watched_status", models.CharField(max_length=300)),
            ],
        ),
    ]

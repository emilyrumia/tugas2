# Generated by Django 4.1 on 2022-09-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mywatchlist", "0005_alter_watchlist_rating_movie_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchlist",
            name="watched_status",
            field=models.CharField(max_length=200),
        ),
    ]

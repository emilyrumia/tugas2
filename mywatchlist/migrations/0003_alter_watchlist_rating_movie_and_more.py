# Generated by Django 4.1 on 2022-09-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mywatchlist", "0002_alter_watchlist_title_movie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchlist",
            name="rating_movie",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="watchlist",
            name="release_date",
            field=models.CharField(max_length=100),
        ),
    ]

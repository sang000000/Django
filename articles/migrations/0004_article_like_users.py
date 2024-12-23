# Generated by Django 5.1.4 on 2024-12-23 11:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_comment_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="like_users",
            field=models.ManyToManyField(
                related_name="like_articles", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
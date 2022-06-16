# Generated by Django 3.2.13 on 2022-06-16 18:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20220616_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='blogpost_dislike', to=settings.AUTH_USER_MODEL),
        ),
    ]

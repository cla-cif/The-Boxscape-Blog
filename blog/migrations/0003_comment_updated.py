# Generated by Django 3.2.13 on 2022-06-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220605_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-08-10 19:39

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='list_image',
            field=models.CharField(blank=True, help_text='Paste here a link ending with .jpg .gif .png .jpeg .webp', max_length=200, null=True, validators=[blog.validators.validate_url], verbose_name='Image'),
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-24 04:16

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.png', upload_to=blog.models.upload_to, verbose_name='image'),
        ),
    ]

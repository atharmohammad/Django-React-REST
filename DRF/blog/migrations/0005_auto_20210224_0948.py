# Generated by Django 3.1.5 on 2021-02-24 04:18

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210224_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='posts/default.png', upload_to=blog.models.upload_to, verbose_name='image'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-06-26 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.URLField(max_length=100),
        ),
    ]

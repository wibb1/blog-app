# Generated by Django 4.2.3 on 2023-09-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_websitemeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitemeta',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]

# Generated by Django 3.2 on 2024-02-06 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20240130_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id']},
        ),
    ]

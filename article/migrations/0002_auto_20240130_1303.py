# Generated by Django 3.2 on 2024-01-30 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-updated']},
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='text',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='avatar',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_blogpost_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='category',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='imagen',
            field=models.ImageField(blank=True, default='empty.jpg', null=True, upload_to=''),
        ),
    ]

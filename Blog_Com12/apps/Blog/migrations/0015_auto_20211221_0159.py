# Generated by Django 3.2.9 on 2021-12-21 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_alter_blogpost_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-publicado',)},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='fecha',
            new_name='publicado',
        ),
    ]

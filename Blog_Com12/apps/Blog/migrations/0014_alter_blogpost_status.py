# Generated by Django 3.2.9 on 2021-12-21 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_auto_20211220_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='status',
            field=models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='publicado', max_length=10),
        ),
    ]

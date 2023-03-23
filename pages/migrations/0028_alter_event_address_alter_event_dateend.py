# Generated by Django 4.1.7 on 2023-03-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_remove_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='event',
            name='dateEnd',
            field=models.DateField(blank=True, verbose_name='Data de Finalização do Evento'),
        ),
    ]

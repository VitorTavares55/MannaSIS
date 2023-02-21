# Generated by Django 4.1.7 on 2023-02-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_scholarship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship',
            old_name='name',
            new_name='stype',
        ),
        migrations.AddField(
            model_name='scholarship',
            name='financier',
            field=models.CharField(default=1, max_length=200, verbose_name='Financiador'),
            preserve_default=False,
        ),
    ]

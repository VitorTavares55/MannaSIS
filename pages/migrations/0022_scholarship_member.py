# Generated by Django 4.1.7 on 2023-02-21 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_remove_member_scholarship'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='Member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='pages.member', verbose_name='Membro'),
            preserve_default=False,
        ),
    ]

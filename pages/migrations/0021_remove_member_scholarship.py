# Generated by Django 4.1.7 on 2023-02-21 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_remove_member_bag_member_scholarship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='scholarship',
        ),
    ]

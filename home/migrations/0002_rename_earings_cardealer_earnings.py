# Generated by Django 4.1.7 on 2023-06-25 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardealer',
            old_name='earings',
            new_name='earnings',
        ),
    ]

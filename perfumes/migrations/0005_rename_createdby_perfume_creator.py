# Generated by Django 4.0.4 on 2022-05-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0004_perfume_createdby_perfume_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfume',
            old_name='createdBy',
            new_name='creator',
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-10 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0008_alter_perfume_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfume',
            old_name='brand_name',
            new_name='brand',
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0009_rename_brand_name_perfume_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='notes',
            field=models.CharField(choices=[('Bergamot', 'bergamtot')], default='N/A', max_length=400),
        ),
    ]
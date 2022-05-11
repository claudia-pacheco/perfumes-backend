# Generated by Django 4.0.4 on 2022-05-10 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfumes', '0006_alter_perfume_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfumes', to=settings.AUTH_USER_MODEL),
        ),
    ]

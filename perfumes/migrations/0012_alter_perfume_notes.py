# Generated by Django 4.0.4 on 2022-05-10 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0011_alter_perfume_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='notes',
            field=models.CharField(choices=[('berg', 'Bergamot'), ('b-orange', 'Bitter Orange'), ('g-fruit', 'Grapefruit'), ('lemon', 'Lemongrass'), ('mandarin', 'Mandarin'), ('b-currant', 'Blackcurrant'), ('j-berry', 'Juniper Berry'), ('pear', 'Pear'), ('cherry', 'Cherry Blossom'), ('gard', 'Gardenia'), ('gera', 'Geranium'), ('jas', 'Jasmine'), ('lav', 'Lavender'), ('hed', 'Hedione'), ('lilly', 'Lily of the Valley'), ('mag', 'Magnolia'), ('peo', 'Peony'), ('rose', 'Rose'), ('tub', 'Tuberose'), ('ylg', 'Ylang Ylang'), ('amber', 'Amber'), ('card', 'Cardamom'), ('path', 'Patchouli'), ('saff', 'Saffron'), ('tob', 'Tobacco'), ('van', 'Vanilla'), ('oud', 'Oud'), ('ced', 'Cedarwood'), ('oak', 'Oakmoss'), ('sand', 'Sandalwood'), ('vet', 'Vetiver')], default='N/A', max_length=400),
        ),
    ]

# Generated by Django 2.1.3 on 2019-01-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fahrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=100)),
                ('nachname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fahrzeug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('schlepper', models.CharField(max_length=100)),
                ('fass', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=100)),
                ('nachname', models.CharField(max_length=100)),
                ('straße', models.CharField(max_length=100)),
                ('hausnr', models.IntegerField()),
                ('plz', models.IntegerField()),
                ('stadt', models.CharField(max_length=100)),
                ('aufnehmer', models.BooleanField()),
                ('abgeber', models.BooleanField()),
                ('beförderer', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Lieferungen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_von', models.DateField()),
                ('datum_bis', models.DateField()),
                ('menge', models.FloatField()),
                ('id_abgeber', models.ManyToManyField(related_name='id_abgeber', to='collect.Kunde')),
                ('id_aufnehmer', models.ManyToManyField(related_name='id_aufnehmer', to='collect.Kunde')),
                ('id_beförderer', models.ManyToManyField(related_name='id_beförderer', to='collect.Kunde')),
                ('id_fahrer', models.ManyToManyField(related_name='id_fahrer', to='collect.Fahrer')),
            ],
        ),
        migrations.CreateModel(
            name='Produkte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(max_length=100)),
                ('art', models.CharField(max_length=100)),
                ('datum_untersuchung', models.CharField(max_length=100)),
                ('n', models.FloatField()),
                ('nh4', models.FloatField()),
                ('p', models.FloatField()),
                ('k', models.FloatField()),
                ('ts', models.FloatField()),
                ('bezugsgröße', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='lieferungen',
            name='id_produkt',
            field=models.ManyToManyField(related_name='id_produkte', to='collect.Produkte'),
        ),
    ]

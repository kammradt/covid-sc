# Generated by Django 3.0.5 on 2020-04-23 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_auto_20200421_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateTimeField(auto_now_add=True, verbose_name='Data do Relatório')),
                ('informant_name', models.CharField(max_length=256, verbose_name='Nome do Informante')),
                ('informant_function', models.CharField(max_length=256, verbose_name='Função do Informante')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.Hospital', verbose_name='Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beds', models.CharField(choices=[('UTIA', 'UTI Adulto'), ('UTIP', 'UTI Pediátrica'), ('UTIN', 'UTI Neonatal'), ('CA', 'Clínico Adulto'), ('CP', 'Clínico Pediátrico'), ('CN', 'Clínico Neonatal'), ('VM', 'Leito Símples com Ventilador Mecânico')], default='UTIA', max_length=38, verbose_name='Tipo do Leito')),
                ('total', models.IntegerField(default=0, verbose_name='Quantidade total de leitos')),
                ('total_covid', models.IntegerField(default=0, verbose_name='Quantidade de leitos para Covid-19')),
                ('occupation', models.IntegerField(default=0, verbose_name='Quantidade de leitos ocupados')),
                ('occupation_covid', models.IntegerField(default=0, verbose_name='Quantidade de leitos ocupados por Covid-19')),
                ('total_waiting_uti', models.IntegerField(default=0, verbose_name='Aguardando UTI')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.Report', verbose_name='Relatório')),
            ],
        ),
    ]

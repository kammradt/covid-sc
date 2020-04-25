# Generated by Django 3.0.5 on 2020-04-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0004_hospitaluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='acronym',
            field=models.CharField(default='-', max_length=150, verbose_name='Sigla'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.9 on 2021-11-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_add_field_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_identifier',
            field=models.CharField(blank=True, max_length=200, verbose_name='идентификатор'),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_change_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='фото места'),
        ),
    ]

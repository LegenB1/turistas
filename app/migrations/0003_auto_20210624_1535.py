# Generated by Django 3.2.4 on 2021-06-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210624_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='imagen',
            field=models.ImageField(null=True, upload_to='hoteles'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='rutas'),
        ),
    ]
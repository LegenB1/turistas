# Generated by Django 3.2.4 on 2021-06-30 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_hotel_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='estrellas',
            field=models.IntegerField(null=True),
        ),
    ]